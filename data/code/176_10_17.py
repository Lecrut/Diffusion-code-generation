import re

def extract_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_text = "This is a test string with words, including multiple sentences!"
    words = extract_words(sample_text)
    print(words)