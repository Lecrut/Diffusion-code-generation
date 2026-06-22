import re

def reverse_words(sentence):
    words = re.findall(r'\S+', sentence)
    words.reverse()
    reversed_words = ' '.join(words)
    return reversed_words

if __name__ == '__main__':
    sample_sentence = "  Hello   world!  This is a test.  "
    result = reverse_words(sample_sentence)
    print(result)