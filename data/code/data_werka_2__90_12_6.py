def check_or_condition(a: bool, b: bool) -> int:
    return int(bool(a) | bool(b))

if __name__ == '__main__':
    result = check_or_condition(True, False)
    print(result)