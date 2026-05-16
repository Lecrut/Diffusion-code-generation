def process_string(input_str):
    lowercase_str = input_str.lower()
    reversed_case_str = input_str.swapcase()
    return (input_str, lowercase_str, reversed_case_str)
if __name__ == '__main__':
    sample = "Hello World"
    result = process_string(sample)
    print(result)