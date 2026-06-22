def validate_state(a: bool, b: bool, c: bool, d: bool) -> bool:
    def check_priority_1():
        return a

    def check_priority_2():
        return b and (not c)

    def check_priority_3():
        return d and (not (a or b))

    if check_priority_1():
        return True
    if check_priority_2():
        return True
    if check_priority_3():
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        (True, False, False, False),
        (False, True, False, False),
        (False, False, True, True),
        (False, False, False, True),
        (False, True, True, False),
        (True, True, True, True)
    ]
    results = [validate_state(a, b, c, d) for a, b, c, d in test_cases]
    print(results)