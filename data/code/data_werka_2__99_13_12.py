def validate_states(a: bool, b: bool, c: bool, d: bool) -> bool:
    if a:
        return True
    if b and (not c):
        return True
    if d and (not a) and (not b):
        return True
    return False
if __name__ == '__main__':
    results = []
    test_cases = [(True, False, False, False), (False, True, False, False), (False, False, True, True), (False, False, False, True), (False, True, True, True), (True, True, True, True), (False, False, False, False)]
    for a, b, c, d in test_cases:
        res = validate_states(a, b, c, d)
        results.append(res)
    print(results)