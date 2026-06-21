import re

def tokenize_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = []
    seen = set()
    for word in words:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    return unique_words

if __name__ == '__main__':
    sample_text = "Python, Python, and more Python!"
    print(tokenize_text(sample_text))