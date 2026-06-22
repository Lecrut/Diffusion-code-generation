def process_string(input_str):
    LOWERCASE_CONVERSION = str.lower
    REVERSED_CASE_CONVERSION = str.swapcase
    return (input_str, LOWERCASE_CONVERSION(input_str), REVERSED_CASE_CONVERSION(input_str))

if __name__ == '__main__':
    SAMPLE_INPUT = "Hello World"
    result = process_string(SAMPLE_INPUT)
    print(result)