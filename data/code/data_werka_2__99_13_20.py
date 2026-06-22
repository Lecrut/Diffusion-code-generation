def validate_state(a: bool, b: bool, c: bool, d: bool) -> bool:
    if a:
        return True
    if b and (not c):
        return True
    if d:
        return True
    return False
if __name__ == '__main__':
    test_cases = [(True, False, False, False), (False, True, False, False), (False, False, True, False), (False, False, False, True), (False, True, True, False), (False, False, False, False), (True, True, True, True)]
    results = [validate_state(a, b, c, d) for a, b, c, d in test_cases]
    print(results)