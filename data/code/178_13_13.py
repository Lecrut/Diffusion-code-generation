import re

def is_valid_phrase(phrase):
    if not isinstance(phrase, str) or not phrase.strip():
        raise ValueError("Input must be a non-empty string")

def extract_words(phrase):
    is_valid_phrase(phrase)
    return re.findall(r'\b\w+\b', phrase.lower())

if __name__ == '__main__':
    sample_phrase = "This is a complex example phrase with various words and punctuation."
    words = extract_words(sample_phrase)
    print(words)