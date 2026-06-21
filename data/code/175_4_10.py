import re

def extract_words(text):
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_text = "This is an example string for testing purposes"
    extracted_words = extract_words(sample_text)
    print(extracted_words)