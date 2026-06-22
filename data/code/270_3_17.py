if __name__ == '__main__':
    input_string = '  Hello World! This is a test.  '
    result = ''.join(char for char in input_string if char != ' ')
    print(result)