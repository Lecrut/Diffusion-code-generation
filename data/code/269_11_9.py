import string

def extract_punctuation_frequencies(text):
    punctuation_dict = {}
    for char in text:
        if char in string.punctuation:
            punctuation_dict[char] = punctuation_dict.get(char, 0) + 1
    return punctuation_dict

if __name__ == '__main__':
    sample_text = "Hello, world! How are you? I'm fine."
    result = extract_punctuation_frequencies(sample_text)
    print(result)