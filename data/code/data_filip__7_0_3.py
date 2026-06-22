import re

SPECIAL_CHAR_PATTERN = re.compile(r'[^\w\s]')

def contains_special_characters(text: str) -> bool:
    return bool(SPECIAL_CHAR_PATTERN.search(text))

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "Hello@World",
        "NoSpecials123",
        "!@#$%",
        "Just Spaces   "
    ]
    
    for case in test_cases:
        result = contains_special_characters(case)
        print(result)