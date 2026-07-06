import streamlit as st
import random

st.set_page_config(
    page_title="AI Interview Coach Agent",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 AI Interview Coach Agent")
st.markdown("### Prepare for Interviews with Personalized AI Guidance")

st.sidebar.header("Agent Settings")

role = st.sidebar.selectbox(
    "Select Job Role",
    [
        "Java Developer",
        "Python Developer",
        "Data Analyst",
        "Data Scientist",
        "Software Engineer",
        "Business Analyst"
    ]
)

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

question_bank = {
    "Java Developer": [
        "What is OOP?",
        "Explain inheritance in Java.",
        "What is multithreading?",
        "Difference between ArrayList and LinkedList?",
        "What is JVM?"
    ],
    "Python Developer": [
        "What are Python decorators?",
        "Explain list comprehension.",
        "What is a lambda function?",
        "Difference between list and tuple?",
        "What are generators?"
    ],
    "Data Analyst": [
        "What is data cleaning?",
        "Explain VLOOKUP.",
        "What is SQL JOIN?",
        "What is data visualization?",
        "Difference between INNER JOIN and LEFT JOIN?"
    ],
    "Data Scientist": [
        "What is machine learning?",
        "Explain overfitting.",
        "What is feature engineering?",
        "Difference between supervised and unsupervised learning?",
        "What is cross validation?"
    ],
    "Software Engineer": [
        "Explain SDLC.",
        "What is Agile?",
        "Difference between stack and queue?",
        "What are APIs?",
        "Explain database normalization."
    ],
    "Business Analyst": [
        "What is requirement gathering?",
        "What is SWOT analysis?",
        "Explain stakeholder management.",
        "What is BPMN?",
        "Difference between BRD and FRD?"
    ]
}

st.header("📋 Interview Question Generator")

if st.button("Generate Questions"):
    questions = random.sample(question_bank[role], 3)

    st.session_state.questions = questions

if "questions" in st.session_state:
    for i, q in enumerate(st.session_state.questions, start=1):
        st.write(f"**Q{i}. {q}**")

st.divider()

st.header("✍ Answer Evaluation")

answer = st.text_area(
    "Paste your answer here",
    height=150
)

if st.button("Evaluate Answer"):

    score = min(len(answer) // 20, 10)

    if score >= 8:
        feedback = "Excellent answer with good detail."
    elif score >= 5:
        feedback = "Good answer. Add more examples and technical depth."
    else:
        feedback = "Answer is too short. Explain concepts clearly and provide examples."

    st.subheader("Evaluation Result")

    st.metric("Score", f"{score}/10")

    st.success(feedback)

st.divider()

st.header("📚 Personalized Study Plan")

if st.button("Generate Study Plan"):

    plan = {
        "Java Developer": [
            "Core Java",
            "Collections Framework",
            "Multithreading",
            "JDBC",
            "Spring Boot"
        ],
        "Python Developer": [
            "Python Basics",
            "OOP",
            "Decorators",
            "Flask",
            "Django"
        ],
        "Data Analyst": [
            "Excel",
            "SQL",
            "Power BI",
            "Statistics",
            "Data Visualization"
        ],
        "Data Scientist": [
            "Python",
            "Statistics",
            "Machine Learning",
            "Deep Learning",
            "MLOps"
        ],
        "Software Engineer": [
            "DSA",
            "System Design",
            "Databases",
            "APIs",
            "Cloud Basics"
        ],
        "Business Analyst": [
            "Requirement Gathering",
            "Excel",
            "SQL",
            "Power BI",
            "Communication Skills"
        ]
    }

    st.write("### Recommended Topics")

    for topic in plan[role]:
        st.checkbox(topic)

st.divider()

st.header("📊 Agent Summary Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Role", role)
col2.metric("Difficulty", difficulty)
col3.metric("Agent Status", "Active")

st.success("AI Interview Coach Agent Ready")