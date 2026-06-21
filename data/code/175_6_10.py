import re

def split_sentence(sentence, delimiters):
    return re.split('|'.join(map(re.escape, delimiters)), sentence)

if __name__ == '__main__':
    sample_sentence = "Hello,world;this is:Python"
    custom_delimiters = [',', ';', ':']
    print(split_sentence(sample_sentence, custom_delimiters))