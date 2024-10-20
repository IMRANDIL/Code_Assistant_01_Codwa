import requests
import gradio as gr
import json

# url = "http://localhost:11434/generate"  # Adjust to your local Codellama endpoint
 
 
# headers = {
#     'Content-Type': "application/json"
# }
# Define the function to send the request to the locally running Codellama model
def codellama_assistant(prompt):
    url = "http://localhost:11434/api/generate"  # Adjust to your local Codellama endpoint
    # payload = {
    #     "prompt": prompt,
    #     "temperature": 1,  # Matches the temperature set in the modelfile
    #     "top_p": 0.9,
    #     "max_tokens": 150,  # Limit the output length
    #     "model": "Codwa"  # Assuming the model is called Codwa
    # }
    data = {
        'model': "Codwa",
        "prompt": prompt,
        "stream": False
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        # print(response)
        output = response.text
        data_output = json.loads(output)
        return data_output['response']
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Create the Gradio interface
iface = gr.Interface(
    fn=codellama_assistant,
    inputs= gr.Textbox(lines = 4, placeholder="Enter your prompt"),
    outputs="text",
    title="Codwa - Your Code Assistant",
    description="Ask Codwa for help with coding, debugging, or explaining concepts."
)

# Launch the Gradio app
iface.launch()
