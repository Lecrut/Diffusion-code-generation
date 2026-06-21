import re

def find_word_boundaries(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    words = re.findall(r'\b\w+\b', sentence)
    return words

if __name__ == '__main__':
    sample_sentence = "Hello, this is a test string with multiple words."
    extracted_words = find_word_boundaries(sample_sentence)
    print(extracted_words)