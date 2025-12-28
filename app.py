import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

groq_api_key=os.getenv('GROQ_API_KEY')

System_Prompt="You are a helpful assistant"
llm=ChatGroq(api_key=groq_api_key,model='llama-3.3-70b-versatile')
prompt=ChatPromptTemplate.from_messages([
         ("system", System_Prompt),
         ("human","{input}")
    ])

chain=prompt|llm|StrOutputParser()

def main():
    while True:
        user_input=input("You: ")
        if user_input.lower()=="quit":
            print("Goodbye")
            break
        print("Assistant", chain.invoke({"input":user_input}))


if __name__=="__main__":
    main()