import streamlit as st
import os

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Untuk Febbiola", 
    page_icon="💖", 
    layout="centered"
)

# 2. Menyimpan status halaman saat ini (seperti bookmark buku)
if 'halaman' not in st.session_state:
    st.session_state.halaman = 1

# Fungsi untuk pindah halaman
def halaman_selanjutnya():
    if st.session_state.halaman < 4:
        st.session_state.halaman += 1

def halaman_sebelumnya():
    if st.session_state.halaman > 1:
        st.session_state.halaman -= 1

# Fungsi untuk menampilkan gambar (agar tidak error jika foto belum ada)
def tampilkan_foto(nama_file):
    if os.path.exists(nama_file):
        st.image(nama_file, use_column_width=True)
    else:
        # Jika foto belum diupload, tampilkan kotak peringatan
        st.warning(f"📷 (Nanti fotomu akan muncul di sini. Jangan lupa simpan fotonya dengan nama '{nama_file}' di folder ini ya!)")

# 3. KONTEN HALAMAN BUKU
st.markdown("<h2 style='text-align: center; color: #ff4b82;'>Happy 8th Monthsary 💖</h2>", unsafe_allow_html=True)
st.write("---")

# ================= HALAMAN 1 =================
if st.session_state.halaman == 1:
    st.subheader("Halaman 1: Hai, Cantikku.")
    tampilkan_foto("foto_1.jpg")
    st.write("""
    Halo sayang, **Febbiola Duri Valentina Naiborhu**.
    
    Nggak kerasa ya, hari ini kita udah jalan persis 8 bulan bareng-bareng. Sejak 27 Oktober 2025 kemaren, hari-hariku jadi jauh lebih berwarna gara-gara ada kamu. Katanya angka 8 itu bentuknya nggak ada ujungnya, sama kayak rasa sayang aku ke kamu sekarang.
    """)

# ================= HALAMAN 2 =================
elif st.session_state.halaman == 2:
    st.subheader("Halaman 2: Makasih ya...")
    tampilkan_foto("foto_2.jpg")
    st.write("""
    Aku cuma mau bilang makasih banyak udah mau nemenin aku sejauh ini. Kamu itu bukan cuma pacar buat aku, tapi juga tempat aku cerita, tempat aku ketawa, dan tempat aku pulang kalau lagi capek sama keadaan. Bawelnya kamu, manjanya kamu, lucunya kamu... semuanya aku suka.
    """)

# ================= HALAMAN 3 =================
elif st.session_state.halaman == 3:
    st.subheader("Halaman 3: Tentang Kita")
    tampilkan_foto("foto_3.jpg")
    st.write("""
    Pasti ada aja ya kadang berantem-berantem kecilnya kita. Tapi dari situ aku sadar, kalau kita berdua tuh sama-sama mau berjuang buat hubungan ini. Makasih ya sayang, udah selalu sabar ngadepin aku, dan selalu mau ngertiin aku. You're simply the best thing that ever happened to me.
    """)

# ================= HALAMAN 4 =================
elif st.session_state.halaman == 4:
    st.subheader("Halaman 4: Untuk Nanti")
    tampilkan_foto("foto_4.jpg")
    st.write("""
    Selamat tanggal 27, sayang. Jangan bosen-bosen ya sama aku. Semoga kita bisa ngelewatin bulan-bulan, bahkan tahun-tahun berikutnya bareng terus. 
    
    Aku sayang banget sama kamu, Febbiola.
    """)
    st.balloons() # Muncul balon perayaan di halaman terakhir!

st.write("---")

# 4. TOMBOL NAVIGASI BUKU (Kiri dan Kanan)
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.session_state.halaman > 1:
        st.button("⬅️ Sebelumnya", on_click=halaman_sebelumnya)

with col2:
    st.markdown(f"<div style='text-align: center; color: gray;'>Halaman {st.session_state.halaman} dari 4</div>", unsafe_allow_html=True)

with col3:
    if st.session_state.halaman < 4:
        st.button("Selanjutnya ➡️", on_click=halaman_selanjutnya)