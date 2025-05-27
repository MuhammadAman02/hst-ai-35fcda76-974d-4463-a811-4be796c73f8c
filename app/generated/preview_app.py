from nicegui import ui, app
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Configure the application
app.title = "ML Engineer Portfolio"
app.favicon = "🧠"

# Sample data for ML Engineer portfolio
PROFILE = {
    "name": "Alex Johnson",
    "title": "Machine Learning Engineer",
    "photo": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=250&h=250&fit=crop",
    "bio": "Experienced Machine Learning Engineer with 5+ years of experience developing and deploying ML models at scale. Specializing in NLP, computer vision, and recommendation systems with a strong background in Python, TensorFlow, and PyTorch.",
    "email": "alex.johnson@example.com",
    "github": "github.com/alexjohnson",
    "linkedin": "linkedin.com/in/alexjohnson",
    "education": [
        {"degree": "M.S. Computer Science, AI Specialization", "institution": "Stanford University", "year": "2018"},
        {"degree": "B.S. Mathematics and Computer Science", "institution": "University of Washington", "year": "2016"}
    ]
}

SKILLS = {
    "Languages": ["Python", "R", "SQL", "C++", "JavaScript"],
    "ML Frameworks": ["TensorFlow", "PyTorch", "Keras", "Scikit-learn"],
    "Big Data": ["Spark", "Hadoop", "Kafka", "Airflow"],
    "Cloud": ["AWS SageMaker", "Google Cloud AI", "Azure ML"],
    "MLOps": ["Docker", "Kubernetes", "MLflow", "DVC", "GitHub Actions"],
    "Visualization": ["Matplotlib", "Seaborn", "Plotly", "Tableau"]
}

SKILL_RATINGS = {
    "Python": 0.95,
    "TensorFlow": 0.9,
    "PyTorch": 0.85,
    "Scikit-learn": 0.9,
    "NLP": 0.85,
    "Computer Vision": 0.8,
    "MLOps": 0.75,
    "Deep Learning": 0.85,
    "Data Engineering": 0.7,
    "Cloud Deployment": 0.8
}

PROJECTS = [
    {
        "title": "Real-time Object Detection System",
        "description": "Developed a real-time object detection system using YOLOv5 that processes video streams with 30+ FPS on edge devices. Implemented model quantization to reduce model size by 70% while maintaining 95% of accuracy.",
        "technologies": ["PyTorch", "YOLO", "OpenCV", "TensorRT"],
        "image": "https://images.unsplash.com/photo-1567361808960-dec9cb578182?w=500&h=300&fit=crop",
        "github": "https://github.com/alexjohnson/realtime-object-detection"
    },
    {
        "title": "NLP-Powered Customer Support Chatbot",
        "description": "Built an intelligent customer support chatbot using BERT for intent classification and named entity recognition. Reduced customer support response time by 45% and achieved 87% customer satisfaction rate.",
        "technologies": ["TensorFlow", "BERT", "FastAPI", "Redis"],
        "image": "https://images.unsplash.com/photo-1531746790731-6c087fecd65a?w=500&h=300&fit=crop",
        "github": "https://github.com/alexjohnson/nlp-support-chatbot"
    },
    {
        "title": "Recommendation Engine for E-commerce",
        "description": "Designed and implemented a hybrid recommendation system combining collaborative filtering and content-based approaches. Increased conversion rate by 23% and average order value by 17%.",
        "technologies": ["Python", "Spark MLlib", "AWS SageMaker", "PostgreSQL"],
        "image": "https://images.unsplash.com/photo-1661956602868-6ae368943878?w=500&h=300&fit=crop",
        "github": "https://github.com/alexjohnson/ecommerce-recommender"
    },
    {
        "title": "Predictive Maintenance for Industrial Equipment",
        "description": "Created an end-to-end ML pipeline for predictive maintenance using sensor data. Reduced unplanned downtime by 35% and maintenance costs by 25% for a manufacturing client.",
        "technologies": ["Scikit-learn", "Time Series Analysis", "Kafka", "Grafana"],
        "image": "https://images.unsplash.com/photo-1581092921461-7d65ca45393a?w=500&h=300&fit=crop",
        "github": "https://github.com/alexjohnson/predictive-maintenance"
    }
]

EXPERIENCE = [
    {
        "role": "Senior ML Engineer",
        "company": "TechCorp AI",
        "period": "2020 - Present",
        "description": "Lead a team of 5 ML engineers developing computer vision solutions for retail analytics. Architected and deployed ML pipelines processing 10TB+ of video data daily.",
        "achievements": [
            "Improved model accuracy by 15% using novel data augmentation techniques",
            "Reduced inference time by 40% through model optimization and quantization",
            "Implemented CI/CD pipeline for ML models, reducing deployment time from days to hours"
        ]
    },
    {
        "role": "ML Engineer",
        "company": "DataSense Inc.",
        "period": "2018 - 2020",
        "description": "Developed NLP models for sentiment analysis and text classification for social media monitoring platform.",
        "achievements": [
            "Built multilingual sentiment analysis model supporting 12 languages",
            "Implemented real-time processing pipeline handling 50K+ messages per minute",
            "Reduced false positive rate by 30% using advanced entity recognition techniques"
        ]
    },
    {
        "role": "Data Science Intern",
        "company": "AI Research Lab",
        "period": "2017 - 2018",
        "description": "Researched and implemented deep learning models for medical image analysis.",
        "achievements": [
            "Co-authored research paper on tumor detection using convolutional neural networks",
            "Developed data preprocessing pipeline for medical imaging datasets",
            "Created interactive visualization tool for model interpretability"
        ]
    }
]

# Create a responsive layout for the portfolio
@ui.page('/')
def portfolio_page():
    with ui.header().classes('bg-primary text-white'):
        with ui.row().classes('w-full items-center justify-between'):
            ui.label(f"{PROFILE['name']} | {PROFILE['title']}").classes('text-h6 q-ml-md')
            with ui.row():
                ui.link('Home', '#home').classes('text-white q-mx-md')
                ui.link('About', '#about').classes('text-white q-mx-md')
                ui.link('Skills', '#skills').classes('text-white q-mx-md')
                ui.link('Projects', '#projects').classes('text-white q-mx-md')
                ui.link('Experience', '#experience').classes('text-white q-mx-md')
                ui.link('Contact', '#contact').classes('text-white q-mx-md')
    
    # Hero section
    with ui.section().classes('flex items-center justify-center bg-blue-50 py-20').id('home'):
        with ui.column().classes('max-w-4xl items-center text-center'):
            ui.image(PROFILE['photo']).classes('w-48 h-48 rounded-full mb-4 shadow-lg')
            ui.label(PROFILE['name']).classes('text-h3 text-weight-bold text-primary')
            ui.label(PROFILE['title']).classes('text-h5 text-blue-8 mb-4')
            ui.markdown(PROFILE['bio']).classes('text-body1 max-w-2xl')
            with ui.row().classes('q-mt-md'):
                ui.button('View Resume', on_click=lambda: ui.download('resume.pdf')).classes('bg-primary')
                ui.button('Contact Me', on_click=lambda: ui.navigate('#contact')).classes('bg-secondary q-ml-sm')
    
    # About section
    with ui.section().classes('py-16 bg-white').id('about'):
        with ui.column().classes('max-w-4xl mx-auto'):
            ui.label('About Me').classes('text-h4 text-primary text-center q-mb-lg')
            
            with ui.row().classes('items-start q-col-gutter-md'):
                # Left column - Education
                with ui.column().classes('w-1/2'):
                    ui.label('Education').classes('text-h5 text-secondary q-mb-md')
                    for edu in PROFILE['education']:
                        with ui.card().classes('w-full q-mb-md'):
                            ui.label(edu['degree']).classes('text-weight-bold')
                            ui.label(f"{edu['institution']} | {edu['year']}")
                
                # Right column - Contact & Links
                with ui.column().classes('w-1/2'):
                    ui.label('Connect With Me').classes('text-h5 text-secondary q-mb-md')
                    with ui.card().classes('w-full'):
                        with ui.row().classes('items-center q-mb-sm'):
                            ui.icon('email').classes('text-primary q-mr-sm')
                            ui.link(PROFILE['email'], f"mailto:{PROFILE['email']}")
                        with ui.row().classes('items-center q-mb-sm'):
                            ui.icon('code').classes('text-primary q-mr-sm')
                            ui.link('GitHub', f"https://{PROFILE['github']}", new_tab=True)
                        with ui.row().classes('items-center'):
                            ui.icon('work').classes('text-primary q-mr-sm')
                            ui.link('LinkedIn', f"https://{PROFILE['linkedin']}", new_tab=True)
    
    # Skills section
    with ui.section().classes('py-16 bg-blue-50').id('skills'):
        with ui.column().classes('max-w-4xl mx-auto'):
            ui.label('Skills & Expertise').classes('text-h4 text-primary text-center q-mb-lg')
            
            with ui.row().classes('q-col-gutter-md'):
                # Left column - Skill categories
                with ui.column().classes('w-1/2'):
                    for category, skills in SKILLS.items():
                        with ui.card().classes('w-full q-mb-md'):
                            ui.label(category).classes('text-h6 text-primary q-mb-sm')
                            with ui.row().classes('flex-wrap'):
                                for skill in skills:
                                    ui.badge(skill).classes('q-ma-xs text-body2')
                
                # Right column - Skill radar chart
                with ui.column().classes('w-1/2'):
                    with ui.card().classes('w-full'):
                        # Create radar chart for skills
                        def create_radar_chart():
                            categories = list(SKILL_RATINGS.keys())
                            values = list(SKILL_RATINGS.values())
                            
                            fig = go.Figure()
                            
                            fig.add_trace(go.Scatterpolar(
                                r=values,
                                theta=categories,
                                fill='toself',
                                name='Skills',
                                line_color='rgb(25, 118, 210)',
                                fillcolor='rgba(25, 118, 210, 0.3)'
                            ))
                            
                            fig.update_layout(
                                polar=dict(
                                    radialaxis=dict(
                                        visible=True,
                                        range=[0, 1]
                                    )
                                ),
                                showlegend=False,
                                margin=dict(l=70, r=70, t=20, b=20),
                                height=350,
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)'
                            )
                            return fig
                        
                        ui.plotly(create_radar_chart).classes('w-full h-80')
    
    # Projects section
    with ui.section().classes('py-16 bg-white').id('projects'):
        with ui.column().classes('max-w-4xl mx-auto'):
            ui.label('ML Projects').classes('text-h4 text-primary text-center q-mb-lg')
            
            # Projects grid
            with ui.grid(columns=2).classes('q-col-gutter-md'):
                for project in PROJECTS:
                    with ui.card().classes('w-full'):
                        ui.image(project['image']).classes('w-full h-48 object-cover')
                        with ui.card_section():
                            ui.label(project['title']).classes('text-h6 text-primary')
                            ui.markdown(project['description']).classes('text-body2 q-my-sm')
                            with ui.row().classes('flex-wrap q-mt-sm'):
                                for tech in project['technologies']:
                                    ui.badge(tech).classes('q-ma-xs bg-secondary text-white')
                            with ui.row().classes('justify-end q-mt-md'):
                                ui.button('View Project', on_click=lambda url=project['github']: ui.open(url)).classes('bg-primary')
    
    # Experience section
    with ui.section().classes('py-16 bg-blue-50').id('experience'):
        with ui.column().classes('max-w-4xl mx-auto'):
            ui.label('Work Experience').classes('text-h4 text-primary text-center q-mb-lg')
            
            # Timeline-like experience display
            for i, exp in enumerate(EXPERIENCE):
                with ui.card().classes('w-full q-mb-lg'):
                    with ui.row().classes('items-start'):
                        # Left column - Period
                        with ui.column().classes('w-1/6'):
                            ui.label(exp['period']).classes('text-weight-bold text-primary')
                        
                        # Right column - Experience details
                        with ui.column().classes('w-5/6'):
                            ui.label(exp['role']).classes('text-h6 text-weight-bold')
                            ui.label(exp['company']).classes('text-subtitle1 text-secondary')
                            ui.markdown(exp['description']).classes('q-my-sm')
                            
                            ui.label('Key Achievements:').classes('text-weight-bold q-mt-sm')
                            with ui.list():
                                for achievement in exp['achievements']:
                                    ui.list_item(achievement)
    
    # Contact section
    with ui.section().classes('py-16 bg-white').id('contact'):
        with ui.column().classes('max-w-4xl mx-auto items-center'):
            ui.label('Get In Touch').classes('text-h4 text-primary text-center q-mb-lg')
            
            with ui.card().classes('w-full max-w-md'):
                with ui.card_section():
                    ui.label('Contact Form').classes('text-h6')
                
                with ui.card_section().classes('q-gutter-md'):
                    name = ui.input('Name').props('outlined').classes('w-full')
                    email = ui.input('Email').props('outlined type=email').classes('w-full')
                    subject = ui.input('Subject').props('outlined').classes('w-full')
                    message = ui.textarea('Message').props('outlined').classes('w-full')
                    
                    def handle_submit():
                        if not name.value or not email.value or not message.value:
                            ui.notify('Please fill all required fields', color='negative')
                            return
                        
                        # In a real app, this would send an email or store the message
                        ui.notify('Message sent successfully! I will get back to you soon.', color='positive')
                        name.value = ''
                        email.value = ''
                        subject.value = ''
                        message.value = ''
                    
                    ui.button('Send Message', on_click=handle_submit).classes('bg-primary w-full')
    
    # Footer
    with ui.footer().classes('bg-primary text-white py-8'):
        with ui.column().classes('items-center'):
            ui.label(f"© {PROFILE['name']} | {PROFILE['title']} | 2023").classes('q-mb-md')
            with ui.row().classes('q-gutter-md'):
                ui.link(icon='email', on_click=lambda: ui.open(f"mailto:{PROFILE['email']}")).classes('text-white')
                ui.link(icon='code', on_click=lambda: ui.open(f"https://{PROFILE['github']}")).classes('text-white')
                ui.link(icon='work', on_click=lambda: ui.open(f"https://{PROFILE['linkedin']}")).classes('text-white')

# Create the application instance
application = app