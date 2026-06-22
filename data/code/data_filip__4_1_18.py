import re

def count_consonants(word: str) -> int:
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    cleaned = re.sub(r'[^a-zA-Z]', '', word)
    return sum(1 for char in cleaned if char in consonants)

if __name__ == '__main__':
    sample_word = "Hello, World! 123"
    result = count_consonants(sample_word)
    print(result)