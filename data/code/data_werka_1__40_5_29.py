import string

def word_to_first_letter(s):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_string = s.translate(translator)
    words = cleaned_string.split()
    result = {word: word[0] for word in words}
    return result
if __name__ == '__main__':
    sample_input = 'Hello, world! This is a test.'
    print(word_to_first_letter(sample_input))