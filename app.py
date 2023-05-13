from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Harikrishna_Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Harikrishna R Nair"
PAGE_ICON = ":wave:"
NAME = "Harikrishna R Nair"
DESCRIPTION = """
Machine Learning Engineer, assisti
"""
EMAIL = "harikrishnar.official@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/harikrishnarnair/",
    "GitHub": "https://github.com/harikris001",
    "Twitter": "https://twitter.com/TheHarikris",
    "Instagram": "https://www.instagram.com/hari_kris_/"
}
PROJECTS = {
    "🏆 Wild Cats classifier - Deep Learning Model that can predict wild cats from an image": "https://wild-cat-classifier-harikris.streamlit.app/",
    "🚀 Super Mario AI - Reinforcement Learning model of Super Mario Bros": "https://github.com/harikris001/Super-mario-Reinforcement-Learning-V2",
    "🏆 Mask Detector - Deep Learning Object detection model to detect mask": "https://github.com/harikris001/Mask-Detector",
    "🚀 Auto Machine Learning App - Web app to automate machine learning": "https://github.com/harikris001/Auto-MachineLearning-App",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 My Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ B.Tech Graduate in Computer Science Engineering
- ✔️ Strong hands on experience and knowledge in Python and C
- ✔️ Good understanding of WebApps and OOP Concepts
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Pytorch), C-Prog
- 📊 Data Visulization: Seaborn, plotly, matplotlib
- 📚 Modeling: Logistic regression, linear regression, Decision trees
- 🧠 Neural Networks: Efficient-Net, Resnet50, Inception
- 🗄️ Databases: MongoDB, MySQL
"""
)

st.write('\n')
st.subheader("Soft Skills")
st.write(
    """

- 🧏 Languages: English, Malayalam(mother tongue), Hindi
- ✌️ Leadership
- 😎 Problem Solving
- 💪 quick adaptability
- 🧑‍🤝‍🧑 Teamwork
"""
)


# --- WORK Experience ---
st.write('\n')
st.subheader("Work Experienece")
st.write("---")

# --- JOB 1
st.write("🚧", "**Internship | Flutter**")
st.write("05/2021 - 05/2021")
st.write(
    """
- ► Introduction to android app development environment
- ► Introduction to Flutter
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
