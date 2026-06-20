import re

def count_consonants(word: str) -> int:
    pattern = re.compile(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]')
    matches = pattern.findall(word)
    return len(matches)

if __name__ == '__main__':
    sample_word = "Hello, World! 123 _-."
    result = count_consonants(sample_word)
    print(result)