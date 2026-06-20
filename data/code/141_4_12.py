def combine_booleans(*args):
    return all(args) or any((not arg for arg in args))
if __name__ == '__main__':
    print(combine_booleans(True, False, True))
    print(combine_booleans(False, False, False))
    print(combine_booleans(True, True, True))
    print(combine_booleans(not True, not False))