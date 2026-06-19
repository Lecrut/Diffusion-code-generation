import requests

API_BASE = "https://pkapust.iis.p.lodz.pl/ollama_piat/v1"

#qwen3.6:27b
API_KEY_1 = "supersilnetymczasowehasloalamakota1"

#qwen3.6:35b
API_KEY_2 = "supersilnetymczasowehasloalamakota2"

#qwen3.5:122b-a10b
API_KEY_3 = "supersilnetymczasowehasloalamakota3"


payload = {
    "model": "ignored",
    "temperature": 0,
    "messages": [
        {
            "role": "user",
            "content": "What is 2+2?\n\n/no_think"
        }
    ]
}

response = requests.post(
    f"{API_BASE}/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY_1}",
        "Content-Type": "application/json"
    },
    json=payload,
    timeout=300
)

response.raise_for_status()

data = response.json()

print(data["choices"][0]["message"]["content"])

