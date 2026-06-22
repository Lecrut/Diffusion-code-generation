def remove_consecutive_spaces(input_string):
    return ' '.join(input_string.split())

if __name__ == '__main__':
    sample_string = "  This   is  a test string with  extra spaces.  "
    cleaned_string = remove_consecutive_spaces(sample_string)
    print(cleaned_string)