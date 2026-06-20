import requests
from time import time

prompt = '''
Task: Create a script that uses list comprehension or a similar Pythonic technique to generate a list containing the string 'Repeat' repeated 50 times. Ensure the resulting code is clean, readable, and adheres to all Python best practices.
STRICT OUTPUT CONTRACT:
1. Output only raw Python source code. No markdown fences, no prose, no explanations.
2. Return exactly one complete runnable Python module.
3. Include an `if __name__ == '__main__':` block with hard-coded sample values.
4. Never call input(), sys.stdin, argparse required arguments, or any interactive prompt.
5. The sample block must run without user input, command-line arguments, network access, or pre-existing files.
6. The module must define the requested function or class when the task asks for one.
7. Unless the task asks only for tests, the main block must directly call a user-defined function or instantiate/use a user-defined class.
8. The main block must print actual returned or computed values, not a status message.
9. For class tasks, instantiate the class inside the main block and print at least one method call result.
10. For function tasks, call the requested function inside the main block and print its returned value.
11. Do not only print constants, precomputed values, dictionaries, or status strings in the main block.
12. Do not include comments beginning with # unless the task explicitly asks for comments.
13. Do not include docstrings unless the task explicitly asks for docstrings, documentation, or explanation.
14. Do not use placeholders, pass-only blocks, TODOs, NotImplementedError, ellipses, or demonstration-only code.
15. The literal tokens `pass`, `NotImplementedError`, `TODO`, `...`, and `Ellipsis` must not appear anywhere in the output.
16. Every function, class, branch, loop, and exception handler must contain real executable logic.
17. Use clear names and simple executable code instead of comments.
18. Use a small dictionary or mapping table when the task involves lookup, categories, units, or named records. Keep the requested public API intact.
'''


timestart = time()

url = "https://pkapust.iis.p.lodz.pl/ollama_piat/api/chat"

r = requests.post(
    url,
    headers={
        "Authorization": "Bearer supersilnetymczasowehasloalamakota1",
        "Content-Type": "application/json",
    },
    json={
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    },
    timeout=300,
)


total_time = time() - timestart

# print(r.status_code)
# print(r.text)

modelname = r.json()["model"]
print("\n\n---", f"response from the model {modelname} took {total_time:.2f} seconds", "---\n\n")
print(r.json()["message"]["content"])


timestart = time()

r = requests.post(
    url,
    headers={
        "Authorization": "Bearer supersilnetymczasowehasloalamakota2",
        "Content-Type": "application/json",
    },
    json={
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    },
    timeout=300,
)

total_time = time() - timestart

modelname = r.json()["model"]
print("\n\n---", f"response from the model {modelname} took {total_time:.2f} seconds", "---\n\n")
print(r.json()["message"]["content"])


timestart = time()

r = requests.post(
    url,
    headers={
        "Authorization": "Bearer supersilnetymczasowehasloalamakota3",
        "Content-Type": "application/json",
    },
    json={
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    },
    timeout=300,
)

total_time = time() - timestart

modelname = r.json()["model"]
print("\n\n---", f"response from the model {modelname} took {total_time:.2f} seconds", "---\n\n")
print(r.json()["message"]["content"])