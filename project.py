import streamlit as st

# Module data buah
def get_fruit_data():
    data = {
        "apel": {
            "mineral": ["Kalium", "Kalsium", "Magnesium", "Fosfor", "Zat Besi"],
            "khasiat": "Menurunkan risiko penyakit jantung, mengontrol gula darah, meningkatkan kesehatan pencernaan, dan membantu menurunkan berat badan",
            "vitamin": ["Vitamin C", "Vitamin A", "Vitamin K", "Vitamin B6"],
            "gula_tinggi": False
        },
        "pisang": {
            "mineral": ["Kalium", "Magnesium", "Fosfor", "Mangan"],
            "khasiat": "Meningkatkan energi, menjaga kesehatan jantung, membantu pencernaan, dan mengurangi kram otot",
            "vitamin": ["Vitamin B6", "Vitamin C", "Vitamin B9"],
            "gula_tinggi": True
        },
        "melon": {
            "mineral": ["Kalium", "Magnesium", "Kalsium", "Fosfor"],
            "khasiat": "Menjaga hidrasi tubuh, meningkatkan kesehatan kulit, mendukung sistem imun, dan menjaga kesehatan mata",
            "vitamin": ["Vitamin C", "Vitamin A", "Vitamin K", "Folat"],
            "gula_tinggi": False
        },
        "jeruk": {
            "mineral": ["Kalium", "Kalsium", "Magnesium", "Fosfor"],
            "khasiat": "Meningkatkan sistem kekebalan tubuh, mencegah batu ginjal, melindungi sel dari kerusakan, dan menjaga kesehatan kulit",
            "vitamin": ["Vitamin C", "Vitamin A", "Folat", "Vitamin B1"],
            "gula_tinggi": False
        },
        "strawberry": {
            "mineral": ["Kalium", "Magnesium", "Mangan", "Zat Besi"],
            "khasiat": "Mengontrol gula darah, melindungi kesehatan jantung, mencegah kanker, dan meningkatkan fungsi otak",
            "vitamin": ["Vitamin C", "Vitamin K", "Folat", "Vitamin B6"],
            "gula_tinggi": False
        },
        "semangka": {
            "mineral": ["Kalium", "Magnesium", "Fosfor", "Kalsium"],
            "khasiat": "Menghidrasi tubuh, menurunkan tekanan darah, mengurangi peradangan, dan mencegah nyeri otot",
            "vitamin": ["Vitamin C", "Vitamin A", "Vitamin B6", "Vitamin B1"],
            "gula_tinggi": False
        },
        "mangga": {
            "mineral": ["Kalium", "Magnesium", "Tembaga", "Fosfor"],
            "khasiat": "Meningkatkan kesehatan mata, memperkuat sistem imun, mencegah kanker, dan menjaga kesehatan kulit",
            "vitamin": ["Vitamin A", "Vitamin C", "Vitamin E", "Vitamin K"],
            "gula_tinggi": True
        },
        "pepaya": {
            "mineral": ["Kalium", "Magnesium", "Kalsium", "Fosfor"],
            "khasiat": "Melancarkan pencernaan, mengurangi peradangan, menyembuhkan luka, dan meningkatkan kesehatan jantung",
            "vitamin": ["Vitamin C", "Vitamin A", "Vitamin E", "Folat"],
            "gula_tinggi": False
        },
        "alpukat": {
            "mineral": ["Kalium", "Magnesium", "Fosfor", "Zat Besi"],
            "khasiat": "Menjaga kesehatan jantung, menurunkan kolesterol, meningkatkan penyerapan nutrisi, dan baik untuk mata",
            "vitamin": ["Vitamin K", "Vitamin E", "Vitamin C", "Vitamin B6"],
            "gula_tinggi": False
        }
    }
    return data

# Function untuk cek buah ada atau tidak
def cek_buah(nama, data):
    if nama.lower() in data:
        return True
    else:
        return False

# Function untuk tampilkan mineral
def tampilkan_mineral(nama, data):
    if cek_buah(nama, data):
        buah = data[nama.lower()]
        st.subheader(f"🔷 Mineral dalam {nama.title()}")
        for i in range(len(buah["mineral"])):
            st.write(f"• {buah['mineral'][i]}")
    else:
        st.error("Buah tidak ditemukan dalam database!")

# Function untuk tampilkan khasiat
def tampilkan_khasiat(nama, data):
    if cek_buah(nama, data):
        buah = data[nama.lower()]
        st.subheader(f"🌿 Khasiat dan Manfaat {nama.title()}")
        st.write(f"**{buah['khasiat']}**")
    else:
        st.error("Buah tidak ditemukan dalam database!")

# Function untuk tampilkan vitamin
def tampilkan_vitamin(nama, data):
    if cek_buah(nama, data):
        buah = data[nama.lower()]
        st.subheader(f"💊 Vitamin dalam {nama.title()}")
        i = 0
        while i < len(buah["vitamin"]):
            st.write(f"• {buah['vitamin'][i]}")
            i += 1
    else:
        st.error("Buah tidak ditemukan dalam database!")

# Function untuk tampilkan kandungan gula
def tampilkan_gula(nama, data):
    if cek_buah(nama, data):
        buah = data[nama.lower()]
        st.subheader(f"🍬 Kandungan Gula {nama.title()}")
        
        if buah["gula_tinggi"] == True:
            st.warning("⚠️ Buah ini mengandung GULA TINGGI")
        elif buah["gula_tinggi"] == False:
            st.success("✅ Buah ini mengandung GULA RENDAH")
        else:
            st.info("Data gula tidak tersedia")
    else:
        st.error("Buah tidak ditemukan dalam database!")

# Variabel untuk data
data_buah = get_fruit_data()

# Konfigurasi page
st.set_page_config(page_title="Info Buah", page_icon="🍎", layout="wide")

# Sidebar untuk navigasi
st.sidebar.title("🍉 Navigasi")
page = st.sidebar.radio(
    "Pilih Halaman:",
    ["Halaman 1: Mineral", "Halaman 2: Khasiat", "Halaman 3: Vitamin", "Halaman 4: Kandungan Gula"]
)

# Informasi jumlah buah
st.sidebar.markdown("---")
st.sidebar.info(f"📊 Total buah tersedia: **{len(data_buah)}** buah")

# HALAMAN 1: MINERAL
if page == "Halaman 1: Mineral":
    st.title("🍎 Informasi Mineral Buah")
    st.write("Masukkan nama buah untuk mengetahui kandungan mineralnya")
    
    nama_buah = st.text_input("Nama Buah:", key="mineral_input")
    
    if st.button("Cek Mineral", key="btn_mineral"):
        if nama_buah:
            tampilkan_mineral(nama_buah, data_buah)
        else:
            st.warning("Silakan masukkan nama buah!")

# HALAMAN 2: KHASIAT
elif page == "Halaman 2: Khasiat":
    st.title("🌿 Khasiat dan Manfaat Buah")
    st.write("Masukkan nama buah untuk mengetahui khasiat dan manfaat kesehatannya")
    
    nama_buah = st.text_input("Nama Buah:", key="khasiat_input")
    
    if st.button("Cek Khasiat", key="btn_khasiat"):
        if nama_buah:
            tampilkan_khasiat(nama_buah, data_buah)
        else:
            st.warning("Silakan masukkan nama buah!")

# HALAMAN 3: VITAMIN
elif page == "Halaman 3: Vitamin":
    st.title("💊 Informasi Vitamin Buah")
    st.write("Masukkan nama buah untuk mengetahui kandungan vitaminnya")
    
    nama_buah = st.text_input("Nama Buah:", key="vitamin_input")
    
    if st.button("Cek Vitamin", key="btn_vitamin"):
        if nama_buah:
            tampilkan_vitamin(nama_buah, data_buah)
        else:
            st.warning("Silakan masukkan nama buah!")

# HALAMAN 4: KANDUNGAN GULA
elif page == "Halaman 4: Kandungan Gula":
    st.title("🍬 Informasi Kandungan Gula Buah")
    st.write("Masukkan nama buah untuk mengetahui apakah mengandung gula tinggi atau tidak")
    
    nama_buah = st.text_input("Nama Buah:", key="gula_input")
    
    if st.button("Cek Kandungan Gula", key="btn_gula"):
        if nama_buah:
            tampilkan_gula(nama_buah, data_buah)
        else:
            st.warning("Silakan masukkan nama buah!")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("💡 Aplikasi ini menggunakan: page, variabel, if, module, looping, function, else, def, elif")