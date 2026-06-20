def validate_exclusive_flags(flags):
    return flags.count(1) == 1
if __name__ == '__main__':
    print(validate_exclusive_flags([0, 0, 1, 0]))
    print(validate_exclusive_flags([0, 1, 0, 0]))
    print(validate_exclusive_flags([1, 0, 0, 0]))
    print(validate_exclusive_flags([0, 0, 0, 0]))
    print(validate_exclusive_flags([1, 1, 0, 0]))