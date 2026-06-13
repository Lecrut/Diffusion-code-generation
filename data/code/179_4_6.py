import re
def reverse_words(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    words.reverse()
    return words
if __name__ == '__main__':
    sample_sentence1 = "Hello world! This is a test."
    result1 = reverse_words(sample_sentence1)
    print(result1)
    sample_sentence2 = "  Word1, Word2. Word3? "
    result2 = reverse_words(sample_sentence2)
    print(result2)
    sample_sentence3 = "Python is fun."
    result3 = reverse_words(sample_sentence3)
    print(result3)