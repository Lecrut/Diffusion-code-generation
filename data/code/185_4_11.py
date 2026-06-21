import re

def tokenize_text(text):
    punctuation = set(".,!?;:")
    words = []
    current_word = []
    for char in text:
        if char.isalpha():
            current_word.append(char.lower())
        elif ''.join(current_word).strip():
            word = ''.join(current_word)
            if not any(word.endswith(p) for p in punctuation):
                words.append(word)
            current_word = []
    if current_word:
        word = ''.join(current_word)
        if not any(word.endswith(p) for p in punctuation):
            words.append(word)
    return list(dict.fromkeys(words))

if __name__ == '__main__':
    sample_text = "Hello, world! Hello, everyone. Welcome to the world of Python."
    print(tokenize_text(sample_text))