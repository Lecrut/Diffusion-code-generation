def compare_booleans(a: bool, b: bool) -> (bool, str):
    if a == b:
        return True, "=="
    else:
        return False, "!="

if __name__ == '__main__':
    print(compare_booleans(True, True))
    print(compare_booleans(False, True))