def both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    sample_values = {
        (False, False): True,
        (True, False): False,
        (False, True): False,
        (True, True): False
    }
    
    for inputs, expected in sample_values.items():
        result = both_false(*inputs)
        print(f"both_false({inputs[0]}, {inputs[1]}) = {result}, Expected: {expected}")