def remove_spaces(input_string):
    return input_string.replace(" ", "").replace("\t", "").replace("\n", "")

if __name__ == '__main__':
    sample_input = "This is a \tsample string with\nvarious spaces."
    result = remove_spaces(sample_input)
    print(result)