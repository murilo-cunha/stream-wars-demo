"""Main demo application."""
import streamlit as st
from stream_wars import stream_wars

_DEFAULTS = {
    "button_text": "Magic 🪄",
    "intro": "Not that long ago, in an office not so far, far away...",
    "title": "Stream Wars",
    "episode_number": "Episode 0",
    "episode_title": "A NEW COMPONENT",
    "content": (
        "Once upon a time, there was a boy that really liked Streamlit and Star"
        " Wars, but couldn't use a Star Wars 'crawl' of his own. He decided to"
        " take matters into his own hands and create a new component. Legend says"
        " our hero still looks for contributions, and that bugs still lurk in the"
        " dark..."
    ),
}

st.header("Stream Wars")
st.subheader("Change the text below and create your own crawl! 🚀☄️🖖")

inputs = {
    k: st.text_input(f"Enter a custom `{k}`:", value=v) for k, v in _DEFAULTS.items()
}

stream_wars(key=None, **inputs)
