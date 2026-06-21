import re

def extract_words(sentence):
    pattern = r'\b\w{2,}\b'
    words = re.findall(pattern, sentence)
    return words

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence with various words."
    extracted_words = extract_words(sample_sentence)
    print(extracted_words)