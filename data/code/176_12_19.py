def find_alphabetic_words(text):
    return [word for word in text.split() if word.isalpha()]

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test with multiple words."
    alphabetic_words = find_alphabetic_words(sample_text)
    print(alphabetic_words)