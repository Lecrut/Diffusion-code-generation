def separate_characters(input_string, delimiter):
    return delimiter.join(char for char in input_string)

if __name__ == '__main__':
    test_string = "Hello World"
    result = separate_characters(test_string, " ")
    print(result)