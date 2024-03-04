import pandas as pd

import streamlit as st
sns.set(style='dark')

#Memanggil file yang diperlukan
aoti_aqi = pd.read_csv("All_csv_files/aoti_aqi.csv")
dong_aqi = pd.read_csv("All_csv_files/dong_aqi.csv")
guan_aqi = pd.read_csv("All_csv_files/guan_aqi.csv")
aoti_image = "All_csv_files/AQI_Aoti.png"
dong_image = "All_csv_files/AQI_Dongsi.png"
guan_image = "All_csv_files/AQI_Guanyuan.png"
info_image = "All_csv_files/info.jpg"

#Membuat tampilan dashboard
st.title("Air Quality Index :wind_blowing_face:")
st.subheader("AQI Stasiun Aoti Zhongxin, Dongsi, dan Guanyuan pada Tahun 2016")

st.subheader("Info Penting :sparkles:")
st.write("Sebelum membaca gambaran data AQI, mari kita lihat dulu kategori nilai AQI melalui gambar di bawah ini. Yuk cek AQI di daerah sekitar kita juga, masuk kategori mana ya :eyes:")
st.image(info_image, caption = "Sumber: iqair.com", use_column_width = True)
st.write("Pada tahun 2016, rerata AQI pada ketiga stasiun adalah sebagai berikut:")
st.write("- Stasiun Aoti Zhongxin sebesar 136 dengan range rerata per bulan 95-165")
st.write("- Stasiun Dongsi sebesar 140 dengan range rerata per bulan 94-210")
st.write("- Stasiun Guanyuan sebesar 140 dengan range rerata per bulan 92-204")

st.write("Berdasarkan nilai AQI tahunnya, ketiga stasiun tersebut berada di kategori *tidak sehat untuk golongan sensitif*. Nilai AQI pada tiga stasiun tersebut dipengaruhi oleh polutan Partikulat Matter 2.5 (PM2.5) yang merupakan partikel udara berukuran lebih kecil atau sama dengan 2,5 mikrometer.")

st.header("Plot Rerata AQI Per Bulan Tahun 2016")
st.subheader(":station: Stasiun Aoti Zhongxin")
#Memasukkan gambar dari hasil scatter plot di notebook.ipynb
st.image(aoti_image, use_column_width = True)

st.subheader(":station: Stasiun Dongsi")
st.image(dong_image, use_column_width = True)

st.subheader(":station: Stasiun Guanyuan")
st.image(guan_image, use_column_width = True)

st.write("Rerata nilai AQI dalam satu tahun merupakan hasil dari rata-rata nilai AQI selama 12 bulan. Berikut merupakan kategorisasi AQI di setiap bulannya di ketiga stasiun.")
st.write(":station: Stasiun Aoti Zhongxin")

aoti_grouped = aoti_aqi.groupby('Kategori')['AQI'].sum().reset_index()
fig1, ax1 = plt.subplots()
ax1.pie(aoti_grouped['AQI'], explode = (0, 0, 0), labels = aoti_grouped['Kategori'], autopct='%1.1f%%', shadow = True, startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

st.write(":station: Stasiun Dongsi")

dong_grouped = dong_aqi.groupby('Kategori')['AQI'].sum().reset_index()
fig2, ax2 = plt.subplots()
ax2.pie(dong_grouped['AQI'], explode = (0, 0, 0, 0), labels = dong_grouped['Kategori'], autopct='%1.1f%%', shadow = True, startangle=90)
ax2.axis('equal')
st.pyplot(fig2)

st.write(":station: Stasiun Guanyuan")

guan_grouped = guan_aqi.groupby('Kategori')['AQI'].sum().reset_index()
fig3, ax3 = plt.subplots()
ax3.pie(guan_grouped['AQI'], explode = (0, 0, 0, 0), labels = guan_grouped['Kategori'], autopct='%1.1f%%', shadow = True, startangle=90)
ax3.axis('equal')
st.pyplot(fig3)

st.write("Catatan:")
st.write("Penghitungan AQI menggunakan sumber referensi berikut")
url = "https://www.airnow.gov/sites/default/files/2020-05/aqi-technical-assistance-document-sept2018.pdf"
st.link_button("AQI Technical Assistance Document", url)
st.caption("Dashboard oleh Naily S")
