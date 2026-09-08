import os 
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate


from langchain_core.output_parsers import StrOutputParser


### Langsmith Tracking 

#os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')



## Promot Templet 

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked"),
    ("human", "Question: {question}")
])


## Streamlit framework 

st.title("Langchain Demo with Gemma")
input_text = st.text_input("What question in your mind?")

## Ollama gemma model

llm = ollama(model="gemma:2b")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))



