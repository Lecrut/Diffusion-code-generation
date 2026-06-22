import string

def extract_punctuation_frequencies(text):
    punctuation_freq = {}
    for char in text:
        if char in string.punctuation:
            punctuation_freq[char] = punctuation_freq.get(char, 0) + 1
    return punctuation_freq

if __name__ == '__main__':
    sample_text = "Hello, world! How are you? I'm fine."
    result = extract_punctuation_frequencies(sample_text)
    print(result)