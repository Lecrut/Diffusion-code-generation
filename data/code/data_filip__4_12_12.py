import re

def count_consonants(text: str) -> int:
    pattern = '[^aeiouAEIOU\\d\\W_]'
    consonants = re.findall(pattern, text)
    return len(consonants)
if __name__ == '__main__':
    test_string = 'Hello, World! 123'
    result = count_consonants(test_string)
    print(result)