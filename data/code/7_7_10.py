import re

def contains_special_characters(input_str):
    stripped = re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
    return len(input_str) != len(stripped)

if __name__ == '__main__':
    test_strings = ["Hello World", "Hello, World!", "NoSpecialsHere", "Has#Symbol"]
    results = [contains_special_characters(s) for s in test_strings]
    print(results)