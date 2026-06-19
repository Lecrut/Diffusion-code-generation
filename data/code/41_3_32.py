def process_string(input_str):
    lowercase_version = input_str.lower()
    reversed_case_version = ''.join(c.swapcase() for c in input_str)
    return (input_str, lowercase_version, reversed_case_version)

if __name__ == '__main__':
    sample_input = "Python3.8"
    result = process_string(sample_input)
    print(result)