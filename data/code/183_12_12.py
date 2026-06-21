DELIMITER = '\t'

def split_names(input_string):
    return [name.strip() for name in input_string.split(DELIMITER) if name.strip()]

if __name__ == '__main__':
    sample_input = "Alice\tBob\tCharlie\tDavid"
    result = split_names(sample_input)
    print(result)