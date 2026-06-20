import re

def count_consonants(word):
    if not isinstance(word, str):
        word = str(word)
    cleaned_word = re.sub(r'[^a-zA-Z]', '', word)
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyz]', cleaned_word, re.IGNORECASE)
    return len(consonants)

if __name__ == '__main__':
    test_cases = ["Hello, World!", "Python3.10", "!!!xyz!!!", "AEIOU", "rhythm", "Scherzo: 123"]
    for case in test_cases:
        result = count_consonants(case)
        print(result)