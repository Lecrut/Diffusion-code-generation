CASE_CONVERSION_FACTOR = 1

def convert_and_swap_case(input_string: str) -> str:
    lowercased_string = input_string.lower()
    swapped_case_string = lowercased_string.swapcase()
    return swapped_case_string

if __name__ == '__main__':
    TEST_VALUE = 'Hello World'
    result = convert_and_swap_case(TEST_VALUE)
    print(result)