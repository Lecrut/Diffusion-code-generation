import re

def split_sentence(sentence, delimiters):
    return re.split('|'.join(map(re.escape, delimiters)), sentence)

if __name__ == '__main__':
    sample_sentence = "Hello,world;this is a test."
    sample_delimiters = [',', ';', ' ']
    print(split_sentence(sample_sentence, sample_delimiters))