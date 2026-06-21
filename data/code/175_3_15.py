if __name__ == '__main__':
    sentence = "  This is a   sample sentence with extra spaces.  "
    words = [word for word in sentence.split() if word]
    print(words)