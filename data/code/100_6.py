def check_consistency(input1, input2, output):
    expected_output = input1 & input2
    return expected_output == output
if __name__ == '__main__':
    print(check_consistency(1, 0, 0))
    print(check_consistency(1, 1, 1))
    print(check_consistency(0, 1, 0))
    print(check_consistency(0, 0, 0))
    print(check_consistency(1, 0, 1))
    print(check_consistency(0, 1, 1))