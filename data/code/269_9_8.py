import re

def extract_punctuation(text):
    return re.findall(r'[^\w\s]', text)

if __name__ == '__main__':
    sample_text = "Hello, world! How are you doing today? I'm fine, thank you. What about you?"
    print(extract_punctuation(sample_text))