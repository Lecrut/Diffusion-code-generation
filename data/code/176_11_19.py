import re

def split_text(text):
    if not isinstance(text, str) or not text:
        raise ValueError("Input must be a non-empty string.")
    
    return re.split(r'\W+', text)

def find_words(text):
    words = split_text(text)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. Multiple   spaces should be handled."
    print(find_words(sample_text))