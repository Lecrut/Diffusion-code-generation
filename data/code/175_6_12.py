import re

def split_sentence(sentence, delimiters):
    pattern = '|'.join(map(re.escape, delimiters))
    return re.split(pattern, sentence)

if __name__ == '__main__':
    sample_sentence = "Hello,world;this is a test."
    delimiters = [',', ';', ' ']
    result = split_sentence(sample_sentence, delimiters)
    print(result)