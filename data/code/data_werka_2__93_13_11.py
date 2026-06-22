def check_both_false(a: bool, b: bool) -> bool:
    mask = 1 if a else 0
    mask |= 2 if b else 0
    return mask == 0

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)