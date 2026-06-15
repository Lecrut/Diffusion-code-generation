if __name__ == '__main__':
    test_string = "hello world"
    reversed_words = " ".join(test_string.split()[::-1])
    print(reversed_words)