import re

def extract_words(text):
    words = re.findall(r'\b\w+\b', text)
    return words

if __name__ == '__main__':
    sample_text = "Python programming is fun! How are you doing today?"
    extracted_words = extract_words(sample_text)
    print(extracted_words)