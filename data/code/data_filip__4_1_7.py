import re

def count_consonants(word):
    pattern = r'[^a-zA-Z0-9\s]'
    cleaned_word = re.sub(pattern, '', word)
    consonant_pattern = r'[^aeiouAEIOU\s0-9]'
    consonants = re.findall(consonant_pattern, cleaned_word)
    return len(consonants)

if __name__ == '__main__':
    sample_words = [
        "hello",
        "world",
        "Python3.9",
        "Café",
        "ström",
        "12345",
        "!@#$%",
        "a",
        "b",
        "A",
        "B",
        "aeiou",
        "bcdfg",
        "Hello, World!",
        "Rhythm",
        ""
    ]
    for word in sample_words:
        result = count_consonants(word)
        print(result)