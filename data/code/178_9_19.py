import numpy as np

def extract_unique_words(text_array):
    words = np.char.split(text_array)
    flattened_words = np.concatenate(words).flatten()
    unique_words = np.unique(flattened_words)
    return list(unique_words)

if __name__ == '__main__':
    sample_strings = ["Hello World this is a Test String", "This Is A Sample String With Mixed Cases"]
    unique_words_list = extract_unique_words(sample_strings)
    print("Unique Words:", unique_words_list)