def split_sentence(text):
    return text.split(' ')
if __name__ == '__main__':
    test_string = "Hello world this is a test"
    result = split_sentence(test_string)
    print(result)