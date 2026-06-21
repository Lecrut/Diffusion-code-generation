def split_string(input_string):
    return input_string.split()

if __name__ == '__main__':
    sample = "  Hello   world! This is a test.  "
    result = split_string(sample)
    print(result)