import re

def count_consonants(word: str) -> int:
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    consonant_pattern = re.compile(r"[^aeiouAEIOU\s\W\d_]", re.UNICODE)
    matches = consonant_pattern.findall(word)
    return len(matches)

if __name__ == '__main__':
    sample_word = "Hello, World! 123"
    result = count_consonants(sample_word)
    print(result)