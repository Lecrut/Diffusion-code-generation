import re

def reverse_words(sentence):
    if not sentence:
        return sentence
    words = sentence.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog"
    result = reverse_words(sample_sentence)
    print(result)