def are_both_false(a, b):
    return not a and not b

if __name__ == '__main__':
    test_cases = {
        (False, False): True,
        (True, False): False,
        (False, True): False,
        (True, True): False
    }
    
    for inputs, expected in test_cases.items():
        result = are_both_false(*inputs)
        print(f"are_both_false{inputs}: {result == expected}")