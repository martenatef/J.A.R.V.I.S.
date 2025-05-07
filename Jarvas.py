import google.generativeai as genai

API_KEY = "AIzaSyDhPIp3IoU9exN28HWRfNEVyNfQuAAfwg0" 

#  ASCII
def generate_model_name():
    part1 = chr(103) + chr(101)  
    part2 = chr(109) + chr(105) 
    part3 = chr(110) + chr(105)  
    part4 = chr(45) + chr(49)    
    part5 = chr(46) + chr(53)    
    part6 = chr(45) + chr(102)  
    part7 = chr(108) + chr(97)  
    part8 = chr(115) + chr(104)  
    
    return part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8

MODEL_NAME = generate_model_name() #collect the name of the model

genai.configure(api_key=API_KEY) #api=(API"val")

model = genai.GenerativeModel(MODEL_NAME)
chat = model.start_chat()

print("Hello I'm Jarvis, AI model created by Marten Atef")
print("Chat with Jarvis! Type 'exit' to quit.")

while True:        #while looop
    user_input = input("You: ") 
    
    if user_input.lower() == 'exit': 
        print("Jarvis: Goodbye!")
        break
    
    if "what is your" in user_input.lower():
        if "name" in user_input.lower():
            response = "My name is Jarvis, created by Marten Atef."
        else:
            response = "Sorry, I don't know the answer to that question."
    else:
        try:
            response = chat.send_message(user_input)
            response = response.text 
        except google.generativeai.exceptions.APIError as e:
            response = f"API error occurred: {e}"  # api error
        except google.generativeai.exceptions.RequestError as e:
            response = f"Request error occurred: {e}"  # request error
        except Exception as e:
            response = f"An unexpected error occurred: {e}"  # unexpected error
    print("Jarvis:", response)
    
    
    
    