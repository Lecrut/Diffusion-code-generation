def xor_check(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    test_cases = {
        (True, False): True,
        (False, True): True,
        (True, True): False,
        (False, False): False
    }
    
    for inputs, expected in test_cases.items():
        result = xor_check(*inputs)
        print(f"xor_check({inputs[0]}, {inputs[1]}) -> {result}, Expected: {expected}")