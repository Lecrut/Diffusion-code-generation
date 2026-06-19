import re

def first_letters_of_words(input_string):
    words = re.findall('\\b\\w+\\b', input_string)
    first_letters = [word[0] for word in words]
    return first_letters
if __name__ == '__main__':
    sample_input = 'Hello, world! This is a test: does it work? Yes, it does!'
    result = first_letters_of_words(sample_input)
    print(result)