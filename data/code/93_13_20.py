def check_both_false(a: bool, b: bool) -> bool:
    if a:
        return False
    if b:
        return False
    return not (a & b)

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)