def check_single_activation(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    print(check_single_activation(True, False))
    print(check_single_activation(False, True))
    print(check_single_activation(True, True))
    print(check_single_activation(False, False))