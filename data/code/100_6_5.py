def check_consistency(input_a, input_b, output):
    expected_output = input_a and input_b
    return expected_output == output
if __name__ == '__main__':
    print(check_consistency(1, 0, 0))
    print(check_consistency(1, 1, 1))
    print(check_consistency(0, 1, 0))
    print(check_consistency(0, 0, 0))
    print(check_consistency(1, 1, 0))