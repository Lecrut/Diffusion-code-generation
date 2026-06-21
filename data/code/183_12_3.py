def split_names(input_string):
    names = input_string.split('\t')
    return [name.strip() for name in names if name.strip()]

if __name__ == '__main__':
    sample_input = "Alice\tBob\tCharlie\tDavid"
    result = split_names(sample_input)
    print(result)