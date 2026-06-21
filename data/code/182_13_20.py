def separate_characters(input_string):
    SEPARATOR = ','
    return SEPARATOR.join(input_string)

if __name__ == '__main__':
    sample_string = "HelloWorld"
    print(separate_characters(sample_string))