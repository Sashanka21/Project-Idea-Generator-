import os
import openai
import customtkinter 

def generate():
    prompt="Please generate 10 ideas for coding projects."
    language=language_dropdown.get()
    prompt+="The programming language is" +" "+ language +"."
    difficulty = difficulty_value.get()
    prompt+="The difficulty is" +" "+ difficulty +"."

    if checkbox1.get():
        prompt +="This project should include a Database."
    if checkbox2.get():
        prompt +="This project should include a API."



    print(prompt)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content": prompt}
    ]
    )
    answer=response.choices[0].message.content
    print(answer)
    result.insert("0.0",answer)




root = customtkinter.CTk()
root.geometry("750*550")
root.title("ChatGpt Project Idea Generator")

customtkinter.set_appearance_mode("dark")

title_label = customtkinter.CTkLabel(root, text="Project Idea Generator")
font=customtkinter.CTkFont(size=30,weight="bold")

title_label.pack(padx=10,pady=(40,20))

frame = customtkinter.CTkFrame(root)
frame.pack(fill="x",padx=100)

language_frame=customtkinter.CTkFrame(frame)
language_frame.pack(padx=100,pady=(20,5),fill="both")

language_label=customtkinter.CTkLabel(
    language_frame,text="Programming Language",font =customtkinter.CTkFont(weight="bold"))
language_label.pack()
language_dropdown=customtkinter.CTkComboBox(
    language_frame,values=["Python", "Java" , "C++", "JavaScript", "Golang"])
language_dropdown.pack(pady=10)


difficulty_frame=customtkinter.CTkFrame(frame)
difficulty_frame.pack(padx=100,pady=5,fill="both")
difficulty_label=customtkinter.CTkLabel(
    difficulty_frame,text="Project Difficulty",font=customtkinter.CTkFont(weight="bold"))

difficulty_label.pack()
difficulty_value=customtkinter.StringVar(value="Easy")

radiobutton1 = customtkinter.CTkRadioButton(
    difficulty_frame,text="Easy",variable=difficulty_value,value="Easy")
radiobutton1.pack(side="left",padx=(20,10),pady=10)

radiobutton2 = customtkinter.CTkRadioButton(
    difficulty_frame,text="Medium",variable=difficulty_value,value="Medium")
radiobutton2.pack(side="left",padx=10,pady=10)

radiobutton3 = customtkinter.CTkRadioButton(
    difficulty_frame,text="Hard",variable=difficulty_value,value="Hard")
radiobutton3.pack(side="left",padx=10,pady=10)



features_frame=customtkinter.CTkFrame(frame)
features_frame.pack(padx=100,pady=5,fill="both")
features_label=customtkinter.CTkLabel(
    features_frame,text="Features",font=customtkinter.CTkFont(weight="bold"))
features_label.pack()
checkbox1 =customtkinter.CTkCheckBox(features_frame,text="Database")
checkbox1.pack(side="left",padx=50,pady=10)
checkbox2 =customtkinter.CTkCheckBox(features_frame,text="API")
checkbox2.pack(side="left",padx=50,pady=10)

button = customtkinter.CTkButton(frame,text="Generate Ideas",command=generate)
button.pack(padx=100,fill="x",pady=(5,20))

result = customtkinter.CTkTextbox(root,font=customtkinter.CTkFont(size=15))
result.pack(pady=10,fill="x",padx=100)




root.mainloop()

