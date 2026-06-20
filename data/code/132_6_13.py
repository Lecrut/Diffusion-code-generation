def verify_status(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    test_cases = [
        (True, False),
        (False, True),
        (True, True),
        (False, False)
    ]
    
    for P_val, Q_val in test_cases:
        result = verify_status(P_val, Q_val)
        print(f"verify_status({P_val}, {Q_val}) = {result}")