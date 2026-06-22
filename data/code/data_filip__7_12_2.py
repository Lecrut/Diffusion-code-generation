import string

def contains_punctuation(text):
    for char in text:
        if char in string.punctuation:
            return True
    return False

if __name__ == '__main__':
    sample1 = "Hello, world!"
    sample2 = "NoPunctuationHere"
    sample3 = "Mix of words, symbols, and 123!"
    print(contains_punctuation(sample1))
    print(contains_punctuation(sample2))
    print(contains_punctuation(sample3))