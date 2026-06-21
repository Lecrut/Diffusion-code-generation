import re

def clean_text(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def find_words(text):
    cleaned_text = clean_text(text)
    return re.findall(r'\b\w+\b', cleaned_text)

if __name__ == '__main__':
    sample_string = "This is a sample string with various words and punctuation! How about this?"
    words = find_words(sample_string)
    print(words)