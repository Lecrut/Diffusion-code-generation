import re

def first_letters_of_words(input_string):
    words = input_string.split()
    result = []
    for word in words:
        cleaned_word = re.sub('^\\W+|\\W+$', '', word)
        if cleaned_word:
            result.append(cleaned_word[0])
    return result
if __name__ == '__main__':
    sample_input_1 = 'Hello, world! This is a test... with some punctuation!!!'
    sample_input_2 = '!@#$%^&*() no words here'
    sample_input_3 = '   Leading spaces and punctuation!!!'
    print(first_letters_of_words(sample_input_1))
    print(first_letters_of_words(sample_input_2))
    print(first_letters_of_words(sample_input_3))