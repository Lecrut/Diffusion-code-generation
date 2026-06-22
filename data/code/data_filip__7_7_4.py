import string

def contains_special_characters(s: str) -> bool:
    stripped = s
    for char in string.punctuation:
        stripped = stripped.replace(char, '')
    return len(stripped) != len(s)

if __name__ == '__main__':
    test_strings = ['hello_world', 'hello world!', 'noSpecialHere', '@#$']
    for s in test_strings:
        result = contains_special_characters(s)
        print(f"String: '{s}' -> Has Special Characters: {result}")