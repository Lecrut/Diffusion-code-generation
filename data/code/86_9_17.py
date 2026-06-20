def compare_booleans(bool1, bool2):
    return f"Boolean comparison result: {bool1} == {bool2} is {bool1 == bool2}"

if __name__ == '__main__':
    print(compare_booleans(True, False))
    print(compare_booleans(False, False))
    print(compare_booleans(True, True))