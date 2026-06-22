import string

def extract_punctuation_frequency(text):
    punctuation_freq = {}
    for char in text:
        if char in string.punctuation:
            punctuation_freq[char] = punctuation_freq.get(char, 0) + 1
    return punctuation_freq

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? This is a test. Numbers 123."
    result = extract_punctuation_frequency(sample_string)
    print(f"Punctuation frequencies in '{sample_string}': {result}")