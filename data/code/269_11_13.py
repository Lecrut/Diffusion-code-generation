import string

def extract_punctuation_frequencies(text):
    punctuation_freq = {char: text.count(char) for char in string.punctuation if char in text}
    return punctuation_freq

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test. It contains various punctuation marks:.,;:'\"!?()[]{}<>"
    result = extract_punctuation_frequencies(sample_text)
    print(result)