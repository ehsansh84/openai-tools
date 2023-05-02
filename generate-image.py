import openai
import requests
from requests.structures import CaseInsensitiveDict

import json

openai.api_key = "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"

def generate_image(prompt):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {openai.api_key}"

    model = "image-alpha-001"
    data = """
    {
        """
    data += f'"model": "{model}",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"512x512",
        "response_format":"url"
    }
    """

    resp = requests.post("https://api.openai.com/v1/images/generations", headers=headers, data=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image")

    response_text = json.loads(resp.text)
    return response_text['data'][0]['url']


prompt = "An realistic angry dragon"
url = generate_image(prompt)
print(url)

