import re

def extract_words(text):
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_text = "Python is an interpreted, high-level and general-purpose programming language."
    words = extract_words(sample_text)
    print(words)