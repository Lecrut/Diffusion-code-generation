import numpy as np

def extract_unique_words(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    
    words = np.char.split(strings, sep=' ')
    flattened_words = [word for sublist in words for word in sublist]
    unique_words = list(set(flattened_words))
    return unique_words

if __name__ == '__main__':
    sample_strings = ["Hello World this is a Test String", "Another Sample with Different Words"]
    unique_word_list = extract_unique_words(sample_strings)
    print("Unique words:", unique_word_list)