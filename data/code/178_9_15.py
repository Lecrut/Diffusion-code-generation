import numpy as np

def extract_unique_words(strings):
    words = np.char.split(strings)
    flattened_words = np.array([word for sublist in words for word in sublist])
    unique_words = np.unique(flattened_words)
    return list(unique_words)

if __name__ == '__main__':
    sample_strings = ["Hello World this is a Test String", "This Is A Sample String With Mixed Cases"]
    unique_word_list = extract_unique_words(sample_strings)
    print("Unique words:", unique_word_list)