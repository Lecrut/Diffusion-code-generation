def verify_status(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    test_cases = [(True, False), (False, True), (True, True), (False, False)]
    results = [verify_status(P, Q) for P, Q in test_cases]
    print(results)