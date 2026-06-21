import re

def count_vowels(text: str) -> int:
    pattern = r"[aeiouAEIOU]"
    matches = re.findall(pattern, text)
    return len(matches)

if __name__ == '__main__':
    test_string = "Hello World! This is a test string with some vowels."
    result = count_vowels(test_string)
    print(result)