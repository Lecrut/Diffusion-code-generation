def remove_spaces(input_string):
    return ''.join(char for char in input_string if char != ' ')

if __name__ == '__main__':
    sample_string = "Python is awesome!"
    result = remove_spaces(sample_string)
    print(result)