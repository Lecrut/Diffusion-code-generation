def check_or_condition(a: bool, b: bool) -> int:
    return int(a) | int(b)

if __name__ == '__main__':
    result = check_or_condition(True, False)
    print(result)