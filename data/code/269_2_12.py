import re

def extract_word_punctuation(sentence):
    pattern = r'(\w+)([^\w\s])'
    matches = re.findall(pattern, sentence)
    return matches

if __name__ == '__main__':
    sample_sentence = "Hello, world! How are you?"
    result = extract_word_punctuation(sample_sentence)
    print(result)