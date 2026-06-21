import re

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).lower()

def tokenize_and_deduplicate(text):
    words = re.findall(r'\b\w+\b', text)
    seen = set()
    unique_words = []
    for word in words:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    return unique_words

if __name__ == '__main__':
    sample_text = "Hello, world! Hello, everyone. Welcome to the world of Python."
    print(tokenize_and_deduplicate(sample_text))