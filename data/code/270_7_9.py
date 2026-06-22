def remove_spaces(input_string):
    translation_table = str.maketrans('', '', ' ')
    return input_string.translate(translation_table)

if __name__ == '__main__':
    sample_string = "Python programming is fun!"
    result = remove_spaces(sample_string)
    print(result)