def check_both_false(a: bool, b: bool) -> bool:
    return int(a) | int(b) == 0
if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)
    result2 = check_both_false(True, False)
    print(result2)