import re

def extract_words(text):
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_text = "This is a test string with words, including multiple sentences!"
    print(extract_words(sample_text))