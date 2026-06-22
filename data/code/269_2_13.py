import re

def extract_word_punctuation_pairs(sentence):
    words_and_punct = re.findall(r'\b\w+\b|[^\w\s]', sentence)
    pairs = [(words_and_punct[i], words_and_punct[i+1]) for i in range(len(words_and_punct)-1)]
    return pairs

if __name__ == '__main__':
    sample_sentence = "Hello, world! How are you?"
    print(extract_word_punctuation_pairs(sample_sentence))