def xor_check(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    test_cases = [
        (True, False),
        (False, True),
        (True, True),
        (False, False)
    ]
    
    for case in test_cases:
        result = xor_check(*case)
        print(f"xor_check({case[0]}, {case[1]}) -> {result}")