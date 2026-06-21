import string

def first_letters_of_words(input_string):
    def is_word(word):
        return any(char.isalpha() for char in word)
    
    words = input_string.split()
    result = [word[0] for word in words if is_word(word)]
    return result

if __name__ == '__main__':
    sample_input_1 = 'Hello, world! This is a test... with some punctuation!!!'
    sample_input_2 = '!@#$%^&*() no words here'
    sample_input_3 = 'Numbers only 123456'
    
    print(first_letters_of_words(sample_input_1))
    print(first_letters_of_words(sample_input_2))
    print(first_letters_of_words(sample_input_3))