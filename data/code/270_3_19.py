def strip_spaces(input_str):
    return input_str.replace(' ', '')

if __name__ == '__main__':
    original_string = "  Python is fun!  "
    no_spaces = strip_spaces(original_string)
    print(no_spaces)