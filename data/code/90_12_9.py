def check_or_condition(a: bool, b: bool) -> bool:
    if a:
        return True
    if b:
        return True
    return False

if __name__ == '__main__':
    result = check_or_condition(False, True)
    print(result)