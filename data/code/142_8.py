def logical_not_comparison(bool1, bool2):
    return not (bool1 == bool2)
if __name__ == '__main__':
    print(logical_not_comparison(True, True))
    print(logical_not_comparison(True, False))
    print(logical_not_comparison(False, True))
    print(logical_not_comparison(False, False))