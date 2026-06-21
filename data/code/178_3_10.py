if __name__ == '__main__':
    phrase = "apple,banana,,orange,,,,grape"
    words = [word.strip(',') for word in phrase.split(',')]
    print(words)