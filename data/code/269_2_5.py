import re

def extract_word_punctuation(sentence):
    words_with_punct = re.findall(r'\b\w+\b[\.,!?]', sentence)
    return [(word, punct) for word, punct in zip(words_with_punct[:-1], words_with_punct[1:])]

if __name__ == '__main__':
    sample_sentence = "Hello, world! How are you?"
    print(extract_word_punctuation(sample_sentence))