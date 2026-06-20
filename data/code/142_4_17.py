def check_xor_difference(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    test_cases = {
        (True, False): True,
        (True, True): False,
        (False, False): False,
        (True, True): False,
        (False, True): True
    }

    for (a, b), expected in test_cases.items():
        result = check_xor_difference(a, b)
        print(f"check_xor_difference({a}, {b}) = {result}, Expected: {expected}")