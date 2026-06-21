def find_alphabetic_words(text):
    return [word for word in text.split() if word.isalpha()]

if __name__ == '__main__':
    sample_text = "Python is an interpreted, high-level and general-purpose programming language."
    alphabetic_words = find_alphabetic_words(sample_text)
    print(alphabetic_words)