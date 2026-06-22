def remove_spaces(input_string):
    return ''.join(filter(lambda char: char != ' ', input_string))

if __name__ == '__main__':
    sample_input = "Python programming is fun!"
    print(remove_spaces(sample_input))