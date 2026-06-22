def is_valid_word(word):
    return word.isalpha()

def find_words(text):
    words = text.split()
    valid_words = [word for word in words if is_valid_word(word)]
    return valid_words

if __name__ == '__main__':
    sample_text = "Hello world this is a test. Python programming is fun and educational!"
    print(find_words(sample_text))