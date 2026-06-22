import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string with 123 numbers."
    print(count_words(sample_text))