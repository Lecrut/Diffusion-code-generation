if __name__ == '__main__':
    PHRASE = "apple,banana,,orange,,,,"
    WORDS = [word for word in PHRASE.split(',') if word]
    print(WORDS)