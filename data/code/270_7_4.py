def remove_spaces(s):
    return s.translate(str.maketrans('', '', ' '))

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    result = remove_spaces(sample_string)
    print(result)