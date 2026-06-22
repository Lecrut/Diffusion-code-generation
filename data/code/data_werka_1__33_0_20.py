def remove_all_spaces(input_string):
    return input_string.replace(" ", "")

if __name__ == '__main__':
    sample_input = "  This is a sample string with spaces   "
    result = remove_all_spaces(sample_input)
    print(result)