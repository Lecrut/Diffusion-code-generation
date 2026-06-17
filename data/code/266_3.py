def word_count(s):
    return len(s.split())
if __name__ == '__main__':
    test_string = "  Hello world  "
    print(word_count(test_string))