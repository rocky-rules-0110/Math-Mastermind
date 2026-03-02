from hf import generate_response
import io 
import streamlit as st
CSS = """<style>
- history-wrap {max-height: 420px; overflow-y: auto; padding-right: 12px; }
- qa-card{
    border: 1px solid #ebebeb;
    background: #ffffff; border-radius: 10px;
    padding: 14px 16px;
    margin: 10px 0;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04)}
•q{font-weight: 700; color: #0a6ebd; margin-bottom: 8px;}
- a{white-space: pre-wrap; color: #333; line-height: 1.5;}"""
def export_bytes (history) :
    text = "join([f"Q{i}: (h['question']}\nA{i}: {h[' answer']}\n\
for i, h in enumerate(history, 1)])
return io.BytesIO(text.encode("utf-8"))
def setup_ui():
st.set_page_config(page_title="AI Teaching Assistant",
layout-"centered" )
st.title("® AI Teaching Assistant")
st.write("Ask me anything about various subjects, and I'll provide an insightful answer.")
st.session_state.setdefault ("history", [])
col_clear, col_export - st.columns ([1, 2]) with col _Clear:
if st.button(" / Clear Conversation"):
st.session_state.history = []
st.rerun)
with col_export:
if st.session_state.history:
st.download_button(
label="& Export Chat History",
data=export_bytes(st.session_state.history),
file_name="chat_history.txt",
mime="text/plain"
)