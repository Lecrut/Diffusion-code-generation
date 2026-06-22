def split_and_filter(input_string):
    return list(filter(lambda s: s.strip(), input_string.split(',')))

if __name__ == '__main__':
    sample_input = "apple,, banana, ,orange, "
    result = split_and_filter(sample_input)
    print(result)