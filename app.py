import streamlit as st
import base64

# Pengaturan Halaman
st.set_page_config(page_title="Dashboard Kuliah SIM", layout="wide")

# --- FUNGSI HEADING (TAMPIL DI TIAP HALAMAN) ---
def tampilkan_heading():
    st.markdown("""
        <div style="background-color:#f8f9fa; padding:25px; border-radius:10px; border-left: 10px solid #007bff; margin-bottom: 30px; text-align: center;">
            <h1 style="color: #1c1e21; margin-bottom: 5px;">SISTEM INFORMASI MANAJEMEN</h1>
            <h3 style="color: #495057; font-weight: normal; margin-bottom: 15px;">Mengembangkan Sistem Informasi Manajemen Layanan Usaha Bisnis Sederhana</h3>
            <hr style="border: 0.5px solid #dee2e6; width: 80%; margin: auto;">
            <div style="margin-top: 15px;">
                <p style="margin: 0; font-weight: bold; color: #343a40; font-size: 1.1em;">Penyusun: Ir. M Nasri AW, M.Eng.Sc, M.Kom</p>
                <p style="margin: 0; color: #6c757d;">Dosen STIE Indonesia Malang, @2025</p>
                <p style="margin: 5px 0 0 0; font-size: 0.9em; color: #007bff; font-weight: 500;">Audiens: Mahasiswa Program Studi Manajemen dan Keuangan</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Fungsi untuk menampilkan PDF
def display_pdf(file_path):
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"⚠️ File '{file_path}' tidak ditemukan di server.")

# Database Materi
materi = {
    "Bab 1": {"judul": "Pendahuluan", "file": "bab 1_Pendahuluan.pdf", "ringkasan": "Definisi MIS, komponen sistem, dan konsep data/informasi."},
    "Bab 2": {"judul": "Analisis Peran Strategi Sistem Informasi Dalam Organisasi", "file": "bab 2_Analisis Peran Strategi Sistem Informasi Dalam Organisasi.pdf", "ringkasan": "Model Porter’s Competitive Forces dan Value Chain."},
    "Bab 3": {"judul": "Identifikasi Jenis-jenis Sistem Dalam Organisasi", "file": "bab 3_Identifikasi Jenis-jenis Sistem Dalam Organisasi.pdf", "ringkasan": "Komponen sistem dan klasifikasi piramida manajemen."},
    "Bab 4": {"judul": "Identifikasi Sistem Untuk Manajemen Tingkat Menengah dan Atas", "file": "bab 4_Identifikasi Sistem Untuk Manajemen Tingkat Menengah dan Atas.pdf", "ringkasan": "Dukungan keputusan melalui MIS, DSS, dan ESS."},
    "Bab 5": {"judul": "Infrastruktur Teknologi Informasi (Hardware dan Software)", "file": "bab 5_Infrastruktur Teknologi Informasi (Hardware dan Software).pdf", "ringkasan": "Hardware, Software, Cloud Computing, dan isu TCO."},
    "Bab 6": {"judul": "Dasar-dasar Manajemen Data dan Pengetahuan", "file": "bab 6_Dasar-dasar Manajemen Data dan Pengetahuan.pdf", "ringkasan": "DBMS, Data Warehouse, Data Mining, dan Business Intelligence."},
    "Bab 7": {"judul": "Proses Pengembangan Sistem", "file": "bab 7_Proses Pengembangan Sistem.pdf", "ringkasan": "Siklus hidup SDLC serta metodologi Waterfall dan Agile."},
    "Bab 8": {"judul": "Solusi Sistem Informasi Terintegrasi Perusahaan", "file": "bab 8_Solusi Sistem Informasi Terintegrasi Perusahaan.pdf", "ringkasan": "Implementasi sistem ERP, CRM, SCM, dan Logistik."},
    "Bab 9": {"judul": "Alat Bantu Untuk Pemodelan Sistem", "file": "bab 9_Alat Bantu Untuk Pemodelan Sistem.pdf", "ringkasan": "Teknik visualisasi menggunakan Use Case, Flowchart, dan DFD."},
    "Bab 10": {"judul": "Telekomunikasi dan Jaringan Dalam Bisnis", "file": "bab 10_Telekomunikasi dan Jaringan Dalam Bisnis.pdf", "ringkasan": "Infrastruktur jaringan, internet, dan model bisnis E-Commerce."},
    "Bab 11": {"judul": "Isu Keamanan dan Kontrol Informasi", "file": "bab 11_Isu Keamanan dan Kontrol Informasi.pdf", "ringkasan": "Manajemen risiko, prinsip CIA Triad, dan kontrol teknis."},
    "Bab 12": {"judul": "Implikasi Etika dan Sosial Teknologi Informasi", "file": "bab 12_Implikasi Etika dan Sosial Teknologi Informasi.pdf", "ringkasan": "Dimensi moral era informasi, privasi data, dan dampak sosial."},
    "Bab 13": {"judul": "Tren Teknologi Masa Depan", "file": "bab 13_Tren Teknologi Masa Depan.pdf", "ringkasan": "Eksplorasi IoT, Big Data, dan Artificial Intelligence."},
    "Bab 14": {"judul": "Tugas dan Presentasi Proyek Akhir Kelompok", "file": "bab 14_Tugas dan Presentasi Proyek Akhir Kelompok.pdf", "ringkasan": "Panduan penyusunan dan teknik presentasi proyek akhir."},
    "Tugas Proyek": {"judul": "Contoh Laporan Proyek Akhir", "file": "Tugas Proyek SIM.pdf", "ringkasan": "Referensi laporan pengembangan SIM (Studi Kasus: Laundry)."},
    "Info UTS-UAS": {"judul": "Panduan Ujian & Tugas", "file": "UTS-UAS.pdf", "ringkasan": "Ketentuan soal UTS, UAS, dan proyek kelompok."}
}

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("cover_sim.png", use_container_width=True)
st.sidebar.title("Navigasi")
selection = st.sidebar.radio(
    "Pilih Halaman:",
    ["Home"] + list(materi.keys()),
    format_func=lambda x: x if x == "Home" else f"{x}: {' '.join(materi[x]['judul'].split()[:3])}{'...' if len(materi[x]['judul'].split()) > 3 else ''}"
)

# --- RENDER DASHBOARD ---

# Tampilkan Heading di setiap halaman (paling atas)
tampilkan_heading()

if selection == "Home":
    st.markdown("""
    ### Selamat Datang di Dashboard Akademik
Platform ini dirancang untuk memudahkan mahasiswa dalam mengakses seluruh materi kuliah secara terintegrasi. 
Gunakan menu di samping kiri untuk mengeksplorasi modul pembelajaran, tugas proyek, dan panduan ujian.

Buku ini disusun dengan bahasa yang sederhana dan mudah dipahami. Kami berharap buku ini dapat membantu mahasiswa memahami Management Information System (Sistem Informasi Manajemen) dengan lebih baik dan dapat mengaplikasikannya dalam praktik manajemen.
Sistematika buku ajar ini, tiap bab dimulai dengan Pokok Bahasan dan Tujuan Pembelajaran, sub bab dan penjelasannya dan Rangkuman, Pertanyaan dan Diskusi serta Daftar Pustaka tiap Bab untuk memperluas bacaan. Tiap bab sesuai pertemuan kuliah (mingguan), minggu ke-8 dilaksanakan Ujian Tengah Semester (UTS) dan minggu ke-16 Ujian Akhir Semester (UAS), dalam bentuk tugas implementasi SIM pada proyek  Mengembangkan Sistem Informasi Manajemen Layanan Usaha Bisnis Sederhana.

Sistematika Bab adalah Bab 1 Pendahuluan; Bab 2 Analisis Peran Strategis Sistem Informasi Dalam Organisasi; Bab 3 Identifikasi Jenis-jenis Sistem Dalam Organisasi; Bab 4 Identifikasi Sistem Untuk Manajemen Tingkat Menengah dan Atas; Bab 5 Infrastruktur Teknologi Informasi (Hardware dan Software); Bab 6 Dasar-dasar Manajemen Data dan Pengetahuan; Bab 7 Proses Pengembangan Sistem; Bab 8 Solusi Sistem Informasi Terintegrasi Perusahaan; Bab 9 Alat Bantu Untuk Pemodelan Sistem; Bab 10 Telekomunikasi dan Jaringan Dalam Bisnis; Bab 11 Isu Keamanan dan Kontrol Informasi; Bab 12 Implikasi Etika dan Sosial Teknologi Informasi; Bab 13 Tren Teknologi Masa Depan; Bab 14 Tugas dan Presentasi Proyek Akhir Kelompok; 
Untuk memberikan pemahaman bagaimana implementasi SIM pada proyek, diberikan contoh lengkap pengerjaan proyek oleh salah satu kelompok mahasiswa, dapat dilihat pada Lampiran Tugas Proyek Mengembangkan SIM Layanan Publik Sederhana.

Panduan Penggunaan:      
    1. Pilih Materi: Klik pada Bab atau Informasi Ujian melalui sidebar.
    2. Ringkasan: Baca poin-poin utama materi pada bagian atas halaman.
    3. Preview PDF: Gunakan penampil dokumen di bawah untuk membaca isi materi secara langsung.
    4. Download: Tombol unduh tersedia jika Anda memerlukan salinan fisik (offline).
    """)
    st.success("Silakan pilih salah satu Bab di navigasi untuk memulai.")

else:
    # Tampilan Halaman Bab/Materi
    data = materi[selection]
    st.subheader(f"{selection}: {data['judul']}")
    
    col_ringkas, col_dl = st.columns([3, 1])
    with col_ringkas:
        st.info(f"**Ringkasan:** {data['ringkasan']}")
    
    with col_dl:
        try:
            with open(data["file"], "rb") as f:
                st.download_button(
                    label=f"📥 Download {selection}",
                    data=f,
                    file_name=data["file"],
                    mime="application/pdf",
                    use_container_width=True
                )
        except:
            st.warning("File tidak ditemukan.")

    st.markdown("---")
    # Penampil PDF Terintegrasi
    display_pdf(data["file"])
