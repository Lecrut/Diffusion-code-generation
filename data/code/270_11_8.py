def remove_consecutive_spaces(input_string):
    return ' '.join(input_string.split())

if __name__ == '__main__':
    sample_input = "  This   is  a   test  string  with  spaces. "
    cleaned_string = remove_consecutive_spaces(sample_input)
    print(cleaned_string)