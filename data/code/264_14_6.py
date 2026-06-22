import re

def extract_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return list(set(words))

if __name__ == '__main__':
    sample_text = "Hello World! This is a test string, with numbers 123 and symbols @#$."
    result = extract_words(sample_text)
    print(result)