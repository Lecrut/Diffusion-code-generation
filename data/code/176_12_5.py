def find_alphabetic_words(text):
    return [word for word in text.split() if word.isalpha()]

if __name__ == '__main__':
    sample_text = "Hello, world! 123 Python 3.8 is fun."
    print(find_alphabetic_words(sample_text))