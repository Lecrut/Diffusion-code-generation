def split_string(input_string):
    return input_string.split()

if __name__ == '__main__':
    sample = "   This is  a test string with multiple spaces. "
    result = split_string(sample)
    print(result)