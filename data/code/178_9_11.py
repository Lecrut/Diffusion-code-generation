import numpy as np

def extract_unique_words(strings):
    words = np.char.split(strings)
    flattened_words = [word for sublist in words for word in sublist]
    unique_words = list(set(flattened_words))
    return unique_words

if __name__ == '__main__':
    sample_strings = ["hello world", "world of programming", "hello everyone"]
    result = extract_unique_words(sample_strings)
    print(result)