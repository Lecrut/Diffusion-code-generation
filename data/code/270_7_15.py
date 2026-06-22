def remove_spaces(input_string):
    return input_string.translate(str.maketrans('', '', ' '))

if __name__ == '__main__':
    sample = "Hello World! This is a test."
    print(remove_spaces(sample))