def separate_characters(input_string, delimiter):
    return ''.join(delimiter + char for char in input_string)

if __name__ == '__main__':
    test_string = "Python"
    delimiter = ", "
    result = separate_characters(test_string, delimiter)
    print(result)