import re
def tokenize_and_unique(text):
    words = re.findall(r'[a-zA-Z]+', text.lower())
    unique_words = set(words)
    return list(unique_words)
if __name__ == '__main__':
    sample_text = "Hello World! This is a test string, with numbers 123 and symbols @#$."
    result = tokenize_and_unique(sample_text)
    print(result)