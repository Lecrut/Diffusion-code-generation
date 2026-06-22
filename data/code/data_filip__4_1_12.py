import re

def count_consonants(word: str) -> int:
    pattern = r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]'
    matches = re.findall(pattern, word)
    return len(matches)

if __name__ == '__main__':
    sample_word = "Hello, World! 123 @#%"
    result = count_consonants(sample_word)
    print(result)