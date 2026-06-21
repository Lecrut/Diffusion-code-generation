if __name__ == '__main__':
    phrase = "apple,banana,,orange,,,,"
    words = [word.strip(',') for word in phrase.split(',') if word.strip(',')]
    print(words)