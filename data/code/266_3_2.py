def count_words(text):
    return len(text.split())
if __name__ == '__main__':
    test_string = "  Hello world  this is a test "
    print(count_words(test_string))