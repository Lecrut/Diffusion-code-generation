import re

def extract_words(text):
    words = re.split(r'\W+', text)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. 123... and punctuation should work."
    result = extract_words(sample_text)
    print(result)