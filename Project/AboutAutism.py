import streamlit as st
from PIL import Image
def app():
    st.header(":blue[Autism Spectrum Disorder]")
    st.write("----")
    with st.container():
        col1,col2= st.columns([3,2])
        with col1:
            st.write("""Autism spectrum disorder (ASD) is a developmental disability caused by differences in the brain. People with ASD often have problems with social communication and interaction, and restricted or repetitive behaviors or interests. People with ASD may also have different ways of learning, moving, or paying attention.
          """)
        with col2:
            img1=Image.open("C:\\Users\\91939\\Downloads\\Project\\1.jpg")
            st.image(img1,width=300)
    st.write("----")        
    with st.container():
        col1,col2= st.columns([4,4])
        with col1:
            st.write("                                              ")
            st.write("                                              ")
            img=Image.open("C:\\Users\\91939\\Downloads\\Project\\2symptoms.jpg")
            st.image(img,width=None,use_column_width=1,caption="Signs of ASD")
           # st.image(img,caption="Signs of ASD")

        with col2:  
            st.header("Symptoms of ASD:")
            st.write(
            """Avoids or does not keep eye contact.
            Does not respond to name by 9 months of age.
            Does not show facial expressions like happy, sad, angry, and surprised by 9 months of age.
            Lines up toys or other objects and gets upset when order is changed.
            Delayed language skills and Delayed movement skills,learning skills.
            Hyperactive, impulsive, and/or inattentive behavior.
            Unusual eating and sleeping habits.
            Anxiety, stress, or excessive worry.
          """)
            st.write("[Learn More >](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders)")   
    with st.container():
        st.title("World Autism Awareness Day")
        c1,c2=st.columns([4,2])
        with c1:
            st.write(
                "The United Nations General Assembly designated 2 April as World Autism Awareness Day (WAAD) in 2007, the United Nations has observed the day as a means to affirm and promote the full realization of all human rights and fundamental freedoms for autistic people on an equal basis with others.")
            st.write("[more information >](https://www.un.org/en/observances/autism-day)")   
        with c2:
            im=Image.open("C:\\Users\\91939\\Downloads\\Project\\3world.png")
            c2.image(im,width=300,caption="",channels="RGB",)