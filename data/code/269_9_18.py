import re

def extract_punctuation(text):

    def is_punctuation_char(char):
        return char in string.punctuation and (not char.isalnum())
    punctuation_marks = []
    for char in text:
        if is_punctuation_char(char):
            punctuation_marks.append(char)
    return punctuation_marks
if __name__ == '__main__':
    sample_string = 'Hello, world! How are you? This is a test.'
    result = extract_punctuation(sample_string)
    print(result)