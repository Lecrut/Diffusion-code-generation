def invert_bitwise_flag(value):
    if value:
        return 0
    return 1

if __name__ == '__main__':
    print(bool(invert_bitwise_flag(True)))
    print(bool(invert_bitwise_flag(False)))