def split_by_space(input_string):
    return input_string.split()

if __name__ == '__main__':
    sample_string = "split this string by spaces"
    result = split_by_space(sample_string)
    print(result)