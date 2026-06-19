from litellm import completion

API_BASE = "https://pkapust.iis.p.lodz.pl/ollama_piat/v1"

#qwen3.6:27b
API_KEY_1 = "supersilnetymczasowehasloalamakota1"

#qwen3.6:35b
API_KEY_2 = "supersilnetymczasowehasloalamakota2"

#qwen3.5:122b-a10b
API_KEY_3 = "supersilnetymczasowehasloalamakota3"

response = completion(
    model="openai/anything",
    api_base=API_BASE,
    api_key=API_KEY_2,
    messages=[
        {
            "role": "user",
            "content": "What is 2+2?\n\n/no_think"
        }
    ],
    temperature=0
)

print(
    response["choices"][0]["message"]["content"]
)

