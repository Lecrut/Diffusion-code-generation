def validate_input_state(a: bool, b: bool, c: bool, d: bool) -> bool:
    if not isinstance(a, bool):
        raise ValueError("a must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("b must be a boolean")
    if not isinstance(c, bool):
        raise ValueError("c must be a boolean")
    if not isinstance(d, bool):
        raise ValueError("d must be a boolean")
    
    if a:
        return True
    if b and not c:
        return True
    if d and not (a or b):
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        (True, False, False, False),
        (False, True, False, False),
        (False, False, True, True),
        (False, False, False, True),
        (False, True, True, False),
        (True, True, True, True),
        (False, False, False, False)
    ]
    results = [validate_input_state(a, b, c, d) for a, b, c, d in test_cases]
    print(results)