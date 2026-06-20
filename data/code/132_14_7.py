def xor(a: bool, b: bool) -> bool:
    return (a + b) % 2 == 1

if __name__ == '__main__':
    test_cases = [
        (True, False),
        (False, True),
        (True, True),
        (False, False)
    ]
    
    for a, b in test_cases:
        result = xor(a, b)
        print(f"xor({a}, {b}) = {result}")