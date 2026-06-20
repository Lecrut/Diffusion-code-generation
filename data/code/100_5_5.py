def check_logic_consistency(input1, input2):
    return input1 and input2
if __name__ == '__main__':
    print(check_logic_consistency(True, True))
    print(check_logic_consistency(False, True))
    print(check_logic_consistency(True, False))
    print(check_logic_consistency(False, False))