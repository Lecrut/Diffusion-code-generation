import re

def count_consonants(text: str) -> int:
    consonant_pattern = re.compile(r'[^aeiouAEIOU\s\W\d_]')
    matches = consonant_pattern.findall(text)
    return len(matches)

if __name__ == '__main__':
    test_string = "Hello, World! 123"
    result = count_consonants(test_string)
    print(result)