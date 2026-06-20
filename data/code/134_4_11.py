def validate_exclusive_flags(flags):
    return bool(flags) == flags & flags - 1 == 0
if __name__ == '__main__':
    print(validate_exclusive_flags([0, 2]))
    print(validate_exclusive_flags([4, 8]))
    print(validate_exclusive_flags([0, 0]))
    print(validate_exclusive_flags([16]))