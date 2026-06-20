def validate_exclusive_flags(flags):
    return (flags[0] & ~sum(flags[1:])) != 0

if __name__ == '__main__':
    print(validate_exclusive_flags([1, 0, 0]))
    print(validate_exclusive_flags([0, 2, 0]))
    print(validate_exclusive_flags([0, 0, 4]))
    print(validate_exclusive_flags([8, 0, 0]))
    print(validate_exclusive_flags([0, 0, 0]))