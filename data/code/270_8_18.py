SPACE = " "

def remove_spaces(input_string):
    return input_string.replace(SPACE, "")

if __name__ == '__main__':
    sample_input = "This is a sample string with spaces"
    result = remove_spaces(sample_input)
    print(result)