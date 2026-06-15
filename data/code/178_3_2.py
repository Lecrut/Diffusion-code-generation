if __name__ == '__main__':
    sentence = "Hello world! How are you?"
    words = [word.rstrip('.,?!') for word in sentence.split()]
    print(words)