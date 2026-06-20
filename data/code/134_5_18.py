XOR = lambda a, b: a and (not b) or (not a and b)

def check_single_activation(a, b):
    return XOR(a, b)
if __name__ == '__main__':
    print(check_single_activation(True, False))
    print(check_single_activation(False, True))
    print(check_single_activation(True, True))
    print(check_single_activation(False, False))