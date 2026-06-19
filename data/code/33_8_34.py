def remove_all_spaces(input_string):
    return ''.join(char for char in input_string if not char.isspace())

if __name__ == '__main__':
    sample_input = "This is a \tsample string.\nIt contains spaces, tabs,\nand newlines."
    result = remove_all_spaces(sample_input)
    print(result)