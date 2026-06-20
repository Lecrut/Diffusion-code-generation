def are_both_false(a, b):
    return not a and not b

if __name__ == '__main__':
    test_cases = {
        (False, False): True,
        (True, False): False,
        (False, True): False,
        (True, True): False
    }
    results = {inputs: are_both_false(*inputs) for inputs in test_cases}
    print(results)