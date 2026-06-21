if __name__ == '__main__':
    phrase = "Python,programming,,is,fun,,and,educational."
    words = [word.strip(',') for word in phrase.split(',')]
    print(words)