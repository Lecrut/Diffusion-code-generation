def process_string(input_str):
    lowercase_version = input_str.lower()
    reversed_case_version = ''.join(c.swapcase() for c in input_str)
    return (input_str, lowercase_version, reversed_case_version)

if __name__ == '__main__':
    sample_text = "Python Programming"
    result_tuple = process_string(sample_text)
    print(result_tuple)