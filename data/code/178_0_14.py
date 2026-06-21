def split_string(input_string):
    return input_string.strip().split()

if __name__ == '__main__':
    sample = "   Hello   world  this is a test   "
    result = split_string(sample)
    print(result)