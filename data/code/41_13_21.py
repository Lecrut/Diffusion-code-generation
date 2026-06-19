def convert_and_swap_case(input_string):
    return input_string.lower().swapcase()

if __name__ == '__main__':
    test_value = 'Hello World'
    result = convert_and_swap_case(test_value)
    print(result)