import re

def tokenize_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words

if __name__ == '__main__':
    sample_text = "Hello, world! Hello, everyone. Welcome to the world of Python."
    print(tokenize_text(sample_text))