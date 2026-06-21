import re

def extract_words(sentence):
    pattern = r'\b\w{2,}\b'
    return re.findall(pattern, sentence)

if __name__ == '__main__':
    sample_sentence = "This is an example sentence with some short and long words."
    print(extract_words(sample_sentence))