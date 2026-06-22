import re

def extract_word_punctuation(sentence):
    words_with_punct = re.findall(r'\b\w+\b[\.,!?]', sentence)
    result = [(word, punct) for word, punct in re.findall(r'(\b\w+\b)([\.,!?])', sentence)]
    return result

if __name__ == '__main__':
    sample_sentence = "Hello, world! How are you?"
    print(extract_word_punctuation(sample_sentence))