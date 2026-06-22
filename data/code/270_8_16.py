def remove_spaces(input_string):
    return "".join(input_string.split())

if __name__ == '__main__':
    sample_string = "  This is a sample string with extra spaces.  "
    processed_string = remove_spaces(sample_string)
    print(processed_string)