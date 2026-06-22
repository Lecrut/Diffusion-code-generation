def convert_and_swap_case(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    lowercased = input_string.lower()
    swapped_case = lowercased.swapcase()
    return swapped_case

if __name__ == '__main__':
    test_value = 'Hello World'
    try:
        result = convert_and_swap_case(test_value)
        print(result)
    except ValueError as e:
        print(e)