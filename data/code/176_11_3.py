import re

def find_words(text):
    return [word for word in re.split(r'\W+', text) if word]

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. Multiple   spaces and punctuation... should work."
    print(find_words(sample_text))