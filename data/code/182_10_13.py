DELIMITER = ', '

def separate_characters(input_string):
    return DELIMITER.join(char for char in input_string)

if __name__ == '__main__':
    test_string1 = "hello"
    result1 = separate_characters(test_string1)
    print(result1)

    test_string2 = "world"
    result2 = separate_characters(test_string2)
    print(result2)

    test_string3 = ""
    result3 = separate_characters(test_string3)
    print(result3)

    test_string4 = "Python"
    result4 = separate_characters(test_string4)
    print(result4)