if __name__ == '__main__':
    test_string = "This is a sample sentence"
    result = " ".join(word[0] for word in test_string.split())
    print(result)