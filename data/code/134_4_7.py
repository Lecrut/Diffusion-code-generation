def validate_exclusive_flags(flags):
    return flags[0] & flags[1] == 0 and flags[0] | flags[1] != 0
if __name__ == '__main__':
    print(validate_exclusive_flags([1, 2]))
    print(validate_exclusive_flags([1, 1]))
    print(validate_exclusive_flags([0, 0]))