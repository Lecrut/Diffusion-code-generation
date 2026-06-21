if __name__ == '__main__':
    sentence = "  Hello   world! This is a test.  "
    words = [word for word in sentence.split() if word]
    print(words)