def compare_booleans(a, b):
    return (not a) == (not b)
if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))