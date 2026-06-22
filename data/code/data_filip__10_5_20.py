import re

def reverse_words(sentence: str) -> str:
    words = re.split(r'\s+', sentence.strip())
    reversed_words = [word for word in reversed(words) if word]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample = "  Hello    World  "
    result = reverse_words(sample)
    print(result)