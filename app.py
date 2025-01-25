import streamlit as st
import random
import time

# Judul aplikasi
st.title("💘 Ramalan Cinta Python 💘")
st.write("Masukkan nama kalian untuk mengetahui tingkat kecocokan cinta!")

# Input nama
nama1 = st.text_input("Nama kamu (contoh: Juned):")
nama2 = st.text_input("Nama dia (contoh: Marni):")

# Tombol untuk menghitung kecocokan
if st.button("Cek Kecocokan"):
    if nama1 and nama2:
        # Placeholder untuk loading
        loading_placeholder = st.empty()

        # Teks loading lucu
        loading_texts = [
            "Menghitung cinta... 💕",
            "Mencari data mantan... 😜",
            "Menguji kesetiaan... 🔍",
            "Menghubungi dukun cinta... 📞",
            "Hampir selesai, sabar dong... ⏳"
        ]

        # Menampilkan loading secara bertahap
        for text in loading_texts:
            loading_placeholder.text(text)
            time.sleep(1)

        # Menghapus placeholder setelah loading selesai
        loading_placeholder.empty()

        # Menghasilkan persentase kecocokan secara acak
        compatibility = random.randint(50, 100)
        st.success(f"{nama1} dan {nama2} cocok {compatibility}%! Tapi cek lagi, mungkin ada bug. 😜")
    else:
        st.error("Harap masukkan kedua nama untuk memulai ramalan!")
