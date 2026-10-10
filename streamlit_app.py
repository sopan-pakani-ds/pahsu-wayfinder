import streamlit as st
import pandas as pd

st.set_page_config(page_title="PAHSU WayFinder", page_icon="📍", layout="centered")

st.markdown("""
<style>
.card{background:white;padding:16px;border-radius:12px;margin-bottom:12px;border-left:5px solid #1e3a8a;box-shadow:0 2px 8px rgba(0,0,0,0.08)}
.room{font-size:22px;font-weight:800;color:#111827}
.badge{background:#dbeafe;color:#1e3a8a;padding:5px 12px;border-radius:20px;font-size:12px;font-weight:700}
.dir{background:#f1f5f9;padding:10px;border-radius:8px;margin-top:8px;font-size:14px}
</style>
""", unsafe_allow_html=True)

st.title("📍 PAHSU WayFinder")
st.caption("Punyashlok Ahilyadevi Holkar Solapur University - Gate QR Navigation")
st.divider()

# Load real Excel - change file name if needed
try:
    df = pd.read_excel("University_Staff_Directory.xlsx")
    # Clean columns
    df.columns = df.columns.str.strip()
except:
    # Fallback dummy if file not found
    data = [
        {"Post": "Director", "names": "Dr. Vikas Tagad", "campus": "new campus", "building": "ahilya bhavan", "floor": "2nd floor", "Direction": "2nd floor right side last cabin", "room no": "215 Director cabin"},
        {"Post": "HOD", "names": "Dr. Pranav Kshirsagar", "campus": "new campus", "building": "ahilya bhavan", "floor": "2nd floor", "Direction": "2nd floor right side", "room no": "232 HOD Cabin"},
        {"Post": "FDO", "names": "Dr. Sopan Yelgunde", "campus": "new campus", "building": "ahilya bhavan", "floor": "2nd floor", "Direction": "2nd floor left side", "room no": "253"},
        {"Post": "Registrar", "names": "Dr. Ramesh Patil", "campus": "old campus", "building": "main building", "floor": "ground floor", "Direction": "straight from main entrance", "room no": "10"},
        {"Post": "Librarian", "names": "Mrs. Anita Deshmukh", "campus": "new campus", "building": "library building", "floor": "ground floor", "Direction": "near reading hall", "room no": "101"},
        {"Post": "System Analyst", "names": "Mr. Rahul Sharma", "campus": "new campus", "building": "ahilya bhavan", "floor": "3rd floor", "Direction": "IT section left wing", "room no": "305"},
    ]
    df = pd.DataFrame(data)

# Search
query = st.text_input("🔍 Search Person / Room", placeholder="Type: Director, HOD, Library, Exam cell...").lower().strip()

if query:
    mask = df.apply(lambda row: query in str(row.values).lower(), axis=1)
    filtered = df[mask]
else:
    filtered = df

st.write(f"**Found {len(filtered)} locations**")

for i, row in filtered.iterrows():
    post = row.get('Post','')
    name = row.get('names','')
    building = row.get('building','')
    floor = row.get('floor','')
    direction = row.get('Direction','')
    room = row.get('room no','')
    campus = row.get('campus','')

    st.markdown(f"""
    <div class="card">
        <span class="badge">{floor} • {building}</span> <span style="font-size:11px;color:#64748b"> {campus}</span>
        <div class="room">📍 Room {room}</div>
        <div style="font-weight:700;margin-top:4px">{post} - {name}</div>
        <div class="dir">🧭 <b>Direction:</b> {direction}<br>🏢 {building}, {floor}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(f"🧭 Get Directions → {post}", key=f"btn_{i}"):
        st.success(f"**{post} - {name}**\n\n📍 Room: {room}\n🏢 {building}, {floor}\n➡️ {direction}")
        st.balloons()

st.divider()
st.info("🔳 **For College Gate:** Deploy this app on Streamlit Cloud and generate QR of the link. One QR for all departments.")