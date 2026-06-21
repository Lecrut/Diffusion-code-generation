import re

TOKEN_PATTERN = r'\b\w+\b'

def tokenize_text(text):
    words = re.findall(TOKEN_PATTERN, text.lower())
    unique_words = []
    seen = set()
    for word in words:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    return unique_words

if __name__ == '__main__':
    sample_text = "Hello, world! Hello, everyone. Welcome to the world of Python."
    print(tokenize_text(sample_text))