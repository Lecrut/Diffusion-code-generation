def split_and_filter(input_string):
    parts = input_string.split(',')
    result = list(filter(lambda x: x.strip() != '', parts))
    return result

if __name__ == '__main__':
    sample_input = "a, b,, c, , d"
    output = split_and_filter(sample_input)
    print(output)