def separate_characters(input_string, delimiter):
    return delimiter.join(input_string)

if __name__ == '__main__':
    test_string = "Hello World"
    delimiter = ", "
    result = separate_characters(test_string, delimiter)
    print(result)