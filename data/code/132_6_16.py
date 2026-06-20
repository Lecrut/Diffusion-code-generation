def verify_status(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    test_cases = {
        (True, False): True,
        (False, True): True,
        (True, True): False,
        (False, False): False
    }
    
    for inputs, expected in test_cases.items():
        result = verify_status(*inputs)
        print(f"Input: {inputs}, Expected: {expected}, Result: {result}")