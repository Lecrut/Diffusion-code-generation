import re

def reverse_words(sentence):
    words = re.findall(r'\S+', sentence)
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    sample_sentence = "Hello   world  this is   a test"
    result = reverse_words(sample_sentence)
    print(result)