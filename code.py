
import requests

# Get user input for the prompt
prompt = input("Enter the prompt: ")

# Make a POST request to the ClipDrop API endpoint
r = requests.post('https://clipdrop-api.co/text-to-image/v1',
  files = {
      'prompt': (None, prompt, 'text/plain')
  },
  headers = { 'x-api-key':'clipboard api key'}
)

# Check if the request was successful
if r.ok:
    # Save the image to a file
    with open('output_image.jpg', 'wb') as f:
        f.write(r.content)
    print("Image saved as 'output_image.jpg'")
else:
    r.raise_for_status()
