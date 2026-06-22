import string

def first_letters_of_words(input_string):
    words = input_string.split()
    result = []
    for word in words:
        stripped_word = word.strip(string.punctuation)
        if stripped_word:
            result.append(stripped_word[0])
    return result
if __name__ == '__main__':
    sample_input = 'Hello, world! This is a test... with punctuation!!!'
    print(first_letters_of_words(sample_input))