def check_both_false(a: bool, b: bool) -> bool:
    return (a ^ b) is False and a is False

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)