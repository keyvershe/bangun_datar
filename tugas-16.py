import streamlit as st

st.set_page_config(page_title="Bangun datar", page_icon="🌟")

st.title("Aplikasi perhitungan bangun datar")
st.write("Silahkan pilih menu di samping untuk memulai")

def luas_persegi(sisi):
    return sisi * sisi

def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

#sidebar
menu = st.sidebar.selectbox("Pilih Bangun Datar", ("Luas Persegi", "Luas Lingkaran", "Luas Segitiga"))

if menu == "Luas Persegi":
    st.header("Luas Persegi")

    #image
    st.image("https://awsimages.detik.net.id/community/media/visual/2025/04/17/persegi-1744886791807_43.png?w=1200", caption="Rumus luas persegi", width=300)

    #input
    sisi = st.number_input("Masukkan panjang sisi persegi:", min_value=0.0)
    if st.button("Hitung"):
        luas = luas_persegi(sisi)
        st.write(f"Luas Persegi dengan sisi {sisi} adalah {luas}")

elif menu == "Luas Lingkaran":
    st.header("Luas Lingkaran")

    #image
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqE7zcAuial5S7kKzPFlfHbDLH-alugkaqYg&s", caption="Rumus luas lingkaran", width=300)

    #input
    jari_jari = st.number_input("Masukkan jari-jari lingkaran:", min_value=0.0)
    if st.button("Hitung"):
        luas = luas_lingkaran(jari_jari)
        st.write(f"Luas Lingkaran dengan jari-jari {jari_jari} adalah {luas}")

elif menu == "Luas Segitiga":
    st.header("Luas Segitiga")

    #image
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_uSKj42nq04jfZCi7cqQ-etlqz8ebdKzb0A&s", caption="Rumus luas segitiga", width=300)

    #input
    alas = st.number_input("Masukkan panjang alas segitiga:", min_value=0.0)
    tinggi = st.number_input("Masukkan tinggi segitiga:", min_value=0.0)
    if st.button("Hitung"):
        luas = luas_segitiga(alas, tinggi)
        st.write(f"Luas Segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}")