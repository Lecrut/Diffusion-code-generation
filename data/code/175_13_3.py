import re
def split_sentence(sentence):
    return re.findall(r'\b\w+\b', sentence)
if __name__ == '__main__':
    sample_sentence = "  Hello world!   This is a test sentence with various spaces. "
    words = split_sentence(sample_sentence)
    print(words)