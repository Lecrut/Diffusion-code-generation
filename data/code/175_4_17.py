import re

def extract_words(sentence):
    WORD_PATTERN = r'\b\w+\b'
    return re.findall(WORD_PATTERN, sentence)

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence for testing purposes."
    words = extract_words(sample_sentence)
    print(words)