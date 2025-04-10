
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Empath: Emotion-Aware Chat", page_icon="💬", layout="centered")

# Custom styles
st.markdown("""
    <style>
        .stChatMessage {font-size: 1.1rem;}
        .user-msg {color: #5E548E;}
        .bot-msg {color: #FF6F91;}
        .bubble {
            border-radius: 20px;
            padding: 10px 15px;
            margin: 10px 0;
            max-width: 80%;
        }
        .user-bubble {
            background-color: #f0e6f6;
            align-self: flex-end;
            margin-left: auto;
        }
        .bot-bubble {
            background-color: #fde2e4;
            align-self: flex-start;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)

st.title("💬 Empath: The Emotion-Aware Chat Companion")
st.markdown("#### Speak your mind. I'll listen with heart. 💖")

if "history" not in st.session_state:
    st.session_state.history = []

def analyze_sentiment(message):
    blob = TextBlob(message)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    else:
        return "neutral"

def generate_response(message):
    sentiment = analyze_sentiment(message)
    if sentiment == "positive":
        return "That's wonderful to hear! 🌟 Keep spreading good vibes!"
    elif sentiment == "negative":
        return "I'm really sorry you're feeling this way. 🫂 Want to talk about it?"
    else:
        return "I'm here for you. Feel free to share more. 💜"

# Chat UI
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:")
    submit = st.form_submit_button("Send")

if submit and user_input:
    st.session_state.history.append(("user", user_input))
    response = generate_response(user_input)
    st.session_state.history.append(("bot", response))

# Display chat history
for sender, message in st.session_state.history:
    bubble_class = "user-bubble" if sender == "user" else "bot-bubble"
    st.markdown(f'<div class="bubble {bubble_class}">{message}</div>', unsafe_allow_html=True)
