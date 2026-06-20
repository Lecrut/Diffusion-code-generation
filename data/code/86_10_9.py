def compare_booleans(a: bool, b: bool) -> str:
    if a == b:
        return 'True/True' if a else 'False/False'
    else:
        return 'True/False' if a else 'False/True'
if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, False))
    print(compare_booleans(True, False))
    print(compare_booleans(False, True))