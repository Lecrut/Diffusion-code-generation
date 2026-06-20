import re

def is_alphanumeric(input_string):
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, input_string))

if __name__ == '__main__':
    test_cases = [
        "Hello123",
        "Hello 123",
        "Hello_123",
        "",
        "1234567890"
    ]
    
    for case in test_cases:
        print(f"'{case}': {is_alphanumeric(case)}")