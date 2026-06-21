def remove_spaces(input_string):
    return input_string.replace(' ', '')
if __name__ == '__main__':
    sample_input = '  This is   a test string with  spaces  '
    result = remove_spaces(sample_input)
    print(result)