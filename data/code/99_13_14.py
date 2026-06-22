def validate_state(a: bool, b: bool, c: bool) -> bool:
    if a:
        return True
    if b and (not c):
        return True
    return False
if __name__ == '__main__':
    test_cases = [(True, True, True), (True, False, False), (False, True, False), (False, True, True), (False, False, False), (False, False, True)]
    results = []
    for a, b, c in test_cases:
        result = validate_state(a, b, c)
        results.append(result)
    print(results)