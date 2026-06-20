def check_both_false(x, y):
    return not x and not y

if __name__ == '__main__':
    test_cases = {
        (False, False): True,
        (True, False): False,
        (False, True): False,
        (True, True): False
    }

    for inputs, expected in test_cases.items():
        result = check_both_false(*inputs)
        print(f"check_both_false({inputs}) -> {result}, Expected: {expected}")