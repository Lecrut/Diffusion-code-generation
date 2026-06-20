def check_both_false(a: bool, b: bool) -> bool:
    if not a and not b:
        return True
    return False

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)