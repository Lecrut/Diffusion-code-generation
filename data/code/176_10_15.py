import re

def extract_words(text):
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_text = "Extracting words from this string using regular expressions is straightforward."
    words = extract_words(sample_text)
    print(words)