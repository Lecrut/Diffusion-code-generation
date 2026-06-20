def check_single_activation(a, b):
    return a != b
if __name__ == '__main__':
    result1 = check_single_activation(True, False)
    print(result1)
    result2 = check_single_activation(False, False)
    print(result2)
    result3 = check_single_activation(True, True)
    print(result3)