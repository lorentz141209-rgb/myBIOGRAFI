from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Data biografi yang dikirimkan ke HTML
    profile_data = {
        "nama": "GILLZZ",
        "sekolah": "MAN 2 Kota Palu",
        "deskripsi": "Siswa yang aktif, berprestasi, dan memiliki ketertarikan tinggi pada dunia ekonomi, teknologi, serta aktivitas organisasi sekolah.",
        "prestasi": [
            "Juara / Penghargaan Perlombaan Siswa (PMR & Organisasi)",
            "Aktif dalam kepengurusan dan kegiatan ekstrakurikuler sekolah",
            "Mewakili MAN 2 Kota Palu dalam ajang kompetisi antar pelajar"
        ],
        "images": ["foto1.jpeg", "foto2.jpg", "foto3.jpg"]
    }
    return render_template('index.html', data=profile_data)

if __name__ == '__main__':
    app.run(debug=True)
