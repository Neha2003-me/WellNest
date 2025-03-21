import streamlit as st

# Function to calculate depression score
def calculate_score(responses):
    return sum(responses)

# Suggestions based on depression level
def get_suggestions(score):
    if 0 <= score <= 4:
        return "You seem to have no depression. Keep maintaining a healthy lifestyle! If you need support, our chatbot is always here to help."
    elif 5 <= score <= 9:
        return "You might have mild depression. Consider practicing self-care and reaching out to loved ones. If you'd like to talk, our chatbot is available for support."
    elif 10 <= score <= 14:
        return "You might have moderate depression. It's important to monitor your feelings and consider speaking with a professional. Our chatbot can guide you further."
    elif 15 <= score <= 19:
        return "You might have moderately severe depression. Please consider consulting a mental health professional soon. Our chatbot can provide resources and support."
    elif 20 <= score <= 27:
        return "You might have severe depression. It's crucial to seek immediate help from a mental health professional. Please reach out, and our chatbot can assist you in finding the right resources."

# Streamlit UI
st.title("Depression Test - WellNest")
st.write("Answer the questions below to assess your mental health. This test is based on the PHQ-9 scale.")

questions = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself, or that you are a failure, or have let yourself or your family down",
    "Trouble concentrating on things, such as reading the newspaper or watching television",
    "Moving or speaking so slowly that other people could have noticed? Or the opposite, being so fidgety or restless that you have been moving around a lot more than usual",
    "Thoughts that you would be better off dead, or of hurting yourself in some way"
]

options = ["Not at all (0 points)", "Several days (1 point)", "More than half the days (2 points)", "Nearly every day (3 points)"]

responses = []
for question in questions:
    response = st.selectbox(question, options, key=question)
    responses.append(options.index(response))

if st.button("Submit"):
    score = calculate_score(responses)
    st.write(f"Your total score is: {score}")
    st.write(get_suggestions(score))

    st.write("If you need help, our chatbot is here to assist you. Click the chatbot icon on the website to start a conversation!")
