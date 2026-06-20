def determine_both_false(val1, val2):
    return not bool(val1) and not bool(val2)

if __name__ == '__main__':
    test_cases = {
        (0, 0): True,
        ('hello', ''): False,
        (None, None): True,
        (True, False): False
    }
    
    for inputs, expected in test_cases.items():
        result = determine_both_false(*inputs)
        print(f"determine_both_false{inputs} -> {result == expected}")