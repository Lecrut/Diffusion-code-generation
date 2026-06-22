import string

def count_punctuation(text):
    punctuation_count = {}
    for char in text:
        if char in string.punctuation:
            punctuation_count[char] = punctuation_count.get(char, 0) + 1
    return punctuation_count

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. It contains various punctuation marks:.,;:'\"!?()[]{}@#$%^&*-_+=|\\/<>"
    result = count_punctuation(sample_text)
    print(result)