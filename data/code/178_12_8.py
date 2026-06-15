import re
def extract_alphabetic_words(sentence):
    words = []
    for char in sentence:
        if char.isalpha():
            words.append(char)
    return list(set(words))
if __name__ == '__main__':
    sample_sentence = "Hello world! This is a test sentence with numbers 123 and symbols @#$"
    result = extract_alphabetic_words(sample_sentence)
    print(result)