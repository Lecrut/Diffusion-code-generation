import re

def count_consonants(word: str) -> int:
    pattern = r'[bcdfghjklmnpqrstvwxyz]'
    matches = re.findall(pattern, word.lower())
    return len(matches)

if __name__ == '__main__':
    result = count_consonants("Hello, World! @#123")
    print(result)