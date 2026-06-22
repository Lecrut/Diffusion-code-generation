import re

def extract_word_punctuation(sentence):
    words_with_punct = re.findall(r'\b\w+\W*\b', sentence)
    result = [(words_with_punct[i], words_with_punct[i+1]) for i in range(len(words_with_punct)-1)]
    return result

if __name__ == '__main__':
    sample_sentence = "Hello, world! How are you?"
    print(extract_word_punctuation(sample_sentence))