import re

def find_first_letter(text):
    pattern = re.compile(r'[a-zA-Z]')
    match = pattern.search(text)
    return match.group(0) if match else None

if __name__ == '__main__':
    test_cases = [
        "123abc",
        "!@#",
        "Hello, World!",
        "",
        "42 is the answer"
    ]
    
    results = {case: find_first_letter(case) for case in test_cases}
    
    for case, result in results.items():
        print(f"Input: '{case}' -> First Letter: {result}")