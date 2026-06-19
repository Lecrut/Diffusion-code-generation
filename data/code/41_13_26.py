def convert_and_swap_case(s):
    return s.lower().swapcase()

if __name__ == '__main__':
    test_value = 'Hello World'
    result = convert_and_swap_case(test_value)
    print(result)