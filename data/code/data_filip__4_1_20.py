import re

def count_consonants(word: str) -> int:
    pattern = r'[bcdfghjklmnpqrstvwxyz]'
    matches = re.findall(pattern, word, re.IGNORECASE)
    return len(matches)

if __name__ == '__main__':
    word = "Hello, World! 123"
    result = count_consonants(word)
    print(result)