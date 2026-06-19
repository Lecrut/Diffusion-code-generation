import string

def word_first_letters(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    words = cleaned_text.split()
    result = {word: word[0] for word in words}
    return result
if __name__ == '__main__':
    sample_text = 'Hello, world! This is a test.'
    print(word_first_letters(sample_text))