import re

def split_non_alphanumeric(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return re.split(r'\W+', text)

def find_words(text):
    words = split_non_alphanumeric(text)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. Multiple   spaces and punctuation... should work."
    print(find_words(sample_text))