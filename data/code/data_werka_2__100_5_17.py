def check_logic_consistency(input_a, input_b):
    expected = input_a and input_b
    return expected

if __name__ == '__main__':
    result = check_logic_consistency(True, False)
    print(result)