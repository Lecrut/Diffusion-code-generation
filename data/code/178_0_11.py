def split_string(input_str):
    return input_str.split()

if __name__ == '__main__':
    sample = "  Hello   world! This is a test.  "
    result = split_string(sample)
    print(result)