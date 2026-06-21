if __name__ == '__main__':
    phrase = "apple,banana,,orange,,,,"
    words = [word for word in phrase.split(',') if word]
    print(words)