TRANSLATE_TABLE = str.maketrans('', '', ' ')

def remove_spaces(input_string):
    return input_string.translate(TRANSLATE_TABLE)

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    print(remove_spaces(sample_string))