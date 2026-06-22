import re

def contains_special_characters(text: str) -> bool:
    pattern = r'[^\w\s]'
    match = re.search(pattern, text)
    return match is not None

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "Hello! World",
        "NoSpecialChars123",
        "Has @ Symbol",
        ""
    ]
    
    for case in test_cases:
        result = contains_special_characters(case)
        print(result)