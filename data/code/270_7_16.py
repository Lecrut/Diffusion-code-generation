def remove_spaces(input_string):
    return input_string.translate(str.maketrans('', '', ' '))

if __name__ == '__main__':
    sample_string = "Python programming is fun!"
    result = remove_spaces(sample_string)
    print(result)