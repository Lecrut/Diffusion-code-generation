def are_equivalent(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    test_cases = [(True, True), (True, False), (False, True), (False, False)]
    for case in test_cases:
        print(are_equivalent(*case))