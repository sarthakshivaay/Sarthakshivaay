import streamlit as st
from PIL import Image
import base64

# Custom CSS for Navbar and Responsiveness
st.markdown("""
    <style>
        /* Style for the navigation bar */
        .navbar {
            padding: 1rem;
            background-color: #16A2CB;
        }

        /* Center the navbar links and ensure even spacing */
        .navbar-nav {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }

        /* Remove bullet points from list items and adjust padding */
        .navbar-nav .nav-link {
            white-space: nowrap;
            padding: 0 2rem;
            list-style: none;
            text-decoration: none;
            color: white;
            font-weight: bold;
        }

        /* Adjust the hover effect */
        .navbar-nav .nav-link:hover {
            color: #ffcc00;
            text-decoration: underline;
        }

        /* Center profile image and adjust margins for responsiveness */
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            max-width: 100%;
            height: auto;
        }

        /* Responsive text size */
        h1, h2, h3, h4, h5 {
            font-size: calc(1.5rem + 1vw);
            text-align: center;
        }

        /* Hide default Streamlit elements */
        #MainMenu, header, footer {visibility: hidden;}
        
        /* Media query for small screens (e.g. phones) */
        @media (max-width: 768px) {
            .navbar-nav .nav-link {
                padding: 0.5rem 1rem;
                font-size: 0.9rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Navbar HTML
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark">
  <a class="navbar-brand" href="https://www.linkedin.com/in/sarthak-tyagi-b34310189/" target="_blank" style="color: white;">Sarthak Tyagi</a>
  <div class="collapse navbar-collapse justify-content-center" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="/">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/sarthakshivaay?tab=repositories">GitHub</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Header
st.write('''# Sarthak Tyagi\n''')

# Profile Image
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Load image as base64
 # Correct path to high-quality image

image_base64 = get_image_base64("images/DSC_4604 a.JPG")  # Correct path to high-quality image


# Custom CSS for the image (Ensure no distortion, border for design)
st.markdown("""
<style>
    .profile-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        width: auto;
        max-width: 250px;
        height: auto;
        border: 4px solid #16A2CB;
    }
</style>
""", unsafe_allow_html=True)

# Embed the image using Base64 in HTML
st.markdown(f"""
    <img src="data:image/jpeg;base64,{image_base64}" alt="Sarthak Tyagi" class="profile-image">
    <h5 style="text-align: center;">Sarthak Tyagi</h5>
""", unsafe_allow_html=True)


# Contact Information
st.markdown('## Contact Info')
st.markdown('Email: sarthaktyagi288@outlook.com')
st.markdown('Phone: (+49) 17629639061')

# Summary
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Endeavoring my 2+ years of experience as an Analyst in the industry and want to broaden my horizons in
 computer science by utilizing my innovative problem-solving, and critical analytical skills and also leveraging
 the programming domains.
''')

# Define the txt function here
def txt(title, dates):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(title)
    with col2:
        st.markdown(dates)

# Education Section
st.markdown('## Education')
st.markdown('**Master of Science** (Artificial Intelligence), *Brandenburg University of Technology*, Cottbus, Germany, Apr 2024 - Present')
st.markdown('**Bachelor of Technology** (Computer Science and Engineering), *SRM University*, Chennai, India, 2017 - 2021')

# Work Experience Section
st.markdown('## Work Experience')

# Analyst Role at IQVIA
txt('**Analyst**, IQVIA, Cottbus, Germany', 'Oct 2021 - Apr 2024')
st.markdown('''
- Provide project delivery support to IQVIA Italy team, including report creation and data analysis.
- Perform data extraction and analytics continuously within strict deadlines.
- Use programming tools such as Matplotlib, SQL, Pandas, and Numpy to manage IT platforms.
- Responsible for system improvement and maintenance.
- Delivered reports ahead of schedule, ensuring team success during renewal periods.
- Assisted another team during a crisis, enabling timely project completion.
- Investigate technical issues using strong data analysis and planning skills.
''')

# Associate Engineer Role at Nagarro
txt('**Associate Engineer**, Nagarro, India', 'Sep 2021 - Oct 2021')
st.markdown('''
- Managed tracking, training, and responding to production inquiries.
- Ensured efficient production issue resolution and task handling on a daily basis.
''')

# Intern Role at Nagarro
txt('**Intern**, Nagarro, India', 'Mar 2021 - Sep 2021')
st.markdown('''
- Worked with C#, HTML, CSS, JavaScript, SQL, and other technologies for project tasks.
- Developed web applications and supported system development on Azure Data Factory.
''')

# Intern Designer Role at Umun Tech
txt('**Intern Designer**, Umun Tech, India', 'Jun 2019 - Jul 2019')
st.markdown('''
- Designed business card applications with UX/UI frameworks like Ionic Framework V3.
- Developed ledger applications with SMS notifications and receipt generation features.
- Implemented using Angular and Typescript.
''')


# Skills Section
st.markdown('## Skills')
st.markdown('**Programming**: Python, C++, C, C#')
st.markdown('**Databases**: MySQL, SQL Server')
st.markdown('**BI Tools**: Power BI')
st.markdown('**MS Office Tools**: MS Excel, POWER APPS')
st.markdown('**Web Technologies**: HTML, CSS, JavaScript, ASP.NET')
st.markdown('**Version Control**: GitHub')

# Projects Section
st.markdown('## Projects')
st.markdown('**Regenix Expert System**: Developed a disease prediction system using Machine Learning, enhancing diagnostic capabilities.')
st.markdown('**Camp Booking**: A web-based platform for online booking using ASP.NET MVC, Entity Framework, SQL Server, and Angular.')
st.markdown('**Northstar**: A Power Apps-based platform for EU HUB (Italy Market definition), focusing on user interface and functionality.')

st.markdown('## Certifications')

st.markdown('''
- **Python 3 Programming Specialization**, University of Michigan (Coursera)
- **Mathematical Thinking in Computer Science**, UC San Diego (Coursera)
- **Power BI Level 100**, IQVIA Visual Analytics (2022)
- **The Bits and Bytes of Computer Networking**, Google (Coursera)
- **Data Science Methodology**, IBM (Coursera)
- **Technical Support Fundamentals**, Google (Coursera)
- **Data Collection and Processing with Python**, University of Michigan (Coursera)
- **Python Certification**, HackerRank (2021)
''')

# Function to create a PDF download button
def get_pdf_download_button(pdf_file_path, button_text):
    with open(pdf_file_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label=button_text, data=PDFbyte, file_name="Sarthak_Resume.pdf", mime='application/octet-stream')

# Adding the download button for the resume PDF
get_pdf_download_button('Sarthak_Resume.pdf', 'Download my Resume as PDF')


