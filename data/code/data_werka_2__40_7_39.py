import re

def first_letters_of_words(input_string: str) -> list:
    words = input_string.split()
    result = []
    for word in words:
        match = re.match('[a-zA-Z]', word)
        if match:
            result.append(match.group())
    return result
if __name__ == '__main__':
    sample_input = 'Hello, world! This is a test... with some punctuation!!!'
    print(first_letters_of_words(sample_input))