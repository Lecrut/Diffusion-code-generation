def convert_and_swap_case(input_string):
    lowercased = input_string.lower()
    swapped_case = lowercased.swapcase()
    return swapped_case

if __name__ == '__main__':
    test_value = 'Hello World'
    result = convert_and_swap_case(test_value)
    print(result)