def check_logic_system(input1, input2):
    return input1 and input2
if __name__ == '__main__':
    print(check_logic_system(True, True))
    print(check_logic_system(False, True))
    print(check_logic_system(True, False))
    print(check_logic_system(False, False))