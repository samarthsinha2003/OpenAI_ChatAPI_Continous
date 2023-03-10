import requests as rq

base_url="https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

content = input("What would you like to ask ChatGPT?\n")
while(content != "Nothing"):
    params = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": content}]
    }
    response = rq.post(url=base_url, headers=headers, json=params)
    print(response.json()["choices"][0]["message"]["content"])
    content = input("\nWhat would you like to ask ChatGPT?\n")
