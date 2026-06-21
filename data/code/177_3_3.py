def split_by_space(input_string):
    return input_string.split()

if __name__ == '__main__':
    test_string = "another string to split"
    result = split_by_space(test_string)
    print(result)