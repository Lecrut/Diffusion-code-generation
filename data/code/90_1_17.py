def check_or_condition(a: bool, b: bool) -> bool:
    conditions = {True: True, False: lambda x, y: x or y}
    return conditions[a](a, b)

if __name__ == '__main__':
    print(check_or_condition(True, False))
    print(check_or_condition(False, True))
    print(check_or_condition(True, True))
    print(check_or_condition(False, False))