def xnor(a: bool, b: bool) -> bool:
    return not (a ^ b)

if __name__ == '__main__':
    test_cases = {
        (True, True): True,
        (False, False): True,
        (True, False): False,
        (False, True): False
    }
    
    for inputs, expected in test_cases.items():
        result = xnor(*inputs)
        print(f"xnor{inputs} = {result}, Expected: {expected}")