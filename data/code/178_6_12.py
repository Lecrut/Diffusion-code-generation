import re
MIN_WORD_LENGTH = 2

def extract_words(sentence):
    pattern = '\\b\\w+\\b'
    words = re.findall(pattern, sentence)
    return [word for word in words if len(word) >= MIN_WORD_LENGTH]
if __name__ == '__main__':
    sample_sentence = 'This is a test sentence with some short and long words.'
    print(extract_words(sample_sentence))