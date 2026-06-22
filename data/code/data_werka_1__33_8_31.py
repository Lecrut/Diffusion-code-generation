def remove_all_spaces(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_input = "This is \t a \n test string with spaces."
    result = remove_all_spaces(sample_input)
    print(result)