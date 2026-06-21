def find_alphabetic_words(text):
    return [word for word in text.split() if word.isalpha()]

if __name__ == '__main__':
    sample_text = "Python, Java, and C++ are programming languages."
    alphabetic_words = find_alphabetic_words(sample_text)
    print(alphabetic_words)