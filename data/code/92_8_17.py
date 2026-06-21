TRUE_MASK = 1
def invert_boolean_bitwise(flag):
    return bool(~flag & TRUE_MASK)
if __name__ == '__main__':
    print(invert_boolean_bitwise(True))
    print(invert_boolean_bitwise(False))