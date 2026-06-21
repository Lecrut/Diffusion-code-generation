def split_string(input_string):
    return input_string.split()

if __name__ == '__main__':
    test_string1 = "this is a sample string"
    words1 = split_string(test_string1)
    print(words1)

    test_string2 = "  leading and trailing spaces   in between "
    words2 = split_string(test_string2)
    print(words2)

    test_string3 = "singleword"
    words3 = split_string(test_string3)
    print(words3)

    test_string4 = ""
    words4 = split_string(test_string4)
    print(words4)