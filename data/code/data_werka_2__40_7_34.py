import string

def first_letters_of_words(input_string):
    def is_alpha(word):
        return any(char.isalpha() for char in word)
    
    words = input_string.split()
    initials = []
    for word in words:
        if is_alpha(word):
            initials.append(word[0])
    return initials

if __name__ == '__main__':
    sample_input_1 = 'Greetings, planet Earth! Welcome to the universe.'
    sample_input_2 = '...No words here just punctuation!!!'
    sample_input_3 = 'Numbers 123 and symbols !@# should be ignored.'
    
    print(first_letters_of_words(sample_input_1))
    print(first_letters_of_words(sample_input_2))
    print(first_letters_of_words(sample_input_3))