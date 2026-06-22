import re

def extract_initials(input_string):
    words = input_string.split()
    initials = []
    for word in words:
        stripped_word = re.sub('^\\W+|\\W+$', '', word)
        if stripped_word:
            initials.append(stripped_word[0])
    return initials
if __name__ == '__main__':
    sample_input_1 = 'Hello, world! This is a test... with some punctuation!!!'
    sample_input_2 = '   Leading spaces and punctuation!!!'
    sample_input_3 = '123numbers only'
    sample_input_4 = '!@#$%^&*() no words here'
    print(extract_initials(sample_input_1))
    print(extract_initials(sample_input_2))
    print(extract_initials(sample_input_3))
    print(extract_initials(sample_input_4))