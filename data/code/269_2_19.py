import re

def extract_word_punctuation(sentence):
    return re.findall(r'\b\w+\b([.,!?])', sentence)

if __name__ == '__main__':
    sample_sentence = "Hello, world! How are you?"
    print(extract_word_punctuation(sample_sentence))