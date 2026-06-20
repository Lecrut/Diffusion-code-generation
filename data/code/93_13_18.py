def both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    sample_values = {
        (False, False): True,
        (True, False): False,
        (False, True): False,
        (True, True): False
    }
    results = {inputs: both_false(*inputs) for inputs in sample_values}
    print(results)