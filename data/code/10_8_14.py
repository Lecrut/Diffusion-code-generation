import re

def reverse_words(sentence: str) -> str:
    words = re.findall(r'\S+', sentence)
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample_text = "Python is powerful and clear"
    result = reverse_words(sample_text)
    print(result)