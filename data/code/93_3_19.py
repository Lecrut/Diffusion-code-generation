def both_false(x, y):
    return not x and not y

if __name__ == '__main__':
    test_cases = {
        (False, False): True,
        (True, False): False,
        (False, True): False,
        (True, True): False
    }
    
    for inputs, expected in test_cases.items():
        result = both_false(*inputs)
        print(f"both_false({inputs[0]}, {inputs[1]}) -> {result}, Expected: {expected}")