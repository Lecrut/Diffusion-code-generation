import re
def separate_words(text):
    words = re.findall(r'[a-zA-Z]+', text)
    return words
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, with various spaces and punctuation."
    sample_string2 = "  Word1, Word2; Word3... "
    sample_string3 = "NoWordsHere"
    print(separate_words(sample_string1))
    print(separate_words(sample_string2))
    print(separate_words(sample_string3))