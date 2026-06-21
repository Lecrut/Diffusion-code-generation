import re

def find_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    return [word for word in re.split(r'\W+', text) if word]

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. Multiple   spaces and punctuation... should work."
    print(find_words(sample_text))