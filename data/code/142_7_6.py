XNOR_CONSTANT = True

def xnor(a: bool, b: bool) -> bool:
    return not a ^ b
if __name__ == '__main__':
    sample1 = xnor(True, True)
    sample2 = xnor(False, False)
    sample3 = xnor(True, False)
    sample4 = xnor(False, True)
    print(sample1)
    print(sample2)
    print(sample3)
    print(sample4)