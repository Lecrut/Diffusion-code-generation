import numpy as np

def extract_unique_words(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    
    words = np.char.split(np.array(strings), sep=' ')
    flat_words = np.concatenate(words).ravel()
    unique_words = list(set(flat_words))
    return unique_words

if __name__ == '__main__':
    sample_strings = ["Hello World this is a Test String", "Sample with Mixed CASES"]
    unique_words = extract_unique_words(sample_strings)
    print("Unique Words:", unique_words)