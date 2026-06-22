def remove_spaces(input_string):
    return input_string.replace(" ", "").replace("\t", "").replace("\n", "")

if __name__ == '__main__':
    sample_input = "This is a sample string.\nIt contains spaces, tabs,\tand newlines."
    result = remove_spaces(sample_input)
    print(result)