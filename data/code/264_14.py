import re
def tokenize_and_filter(text):
    words = set()
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            words.add(char.lower())
    return sorted(list(words))
if __name__ == '__main__':
    sample_text = "Hello World! This is a Test string with numbers 123 and symbols @#$"
    result = tokenize_and_filter(sample_text)
    print(result)