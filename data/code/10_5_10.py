import re

def reverse_words(sentence: str) -> str:
    words = re.findall(r'\S+', sentence)
    return ' '.join(reversed(words))

if __name__ == '__main__':
    result = reverse_words("  Hello   World  ")
    print(result)