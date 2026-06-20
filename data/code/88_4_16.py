def logical_and(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    samples = {
        (True, True): True,
        (True, False): False,
        (False, True): False,
        (False, False): False
    }
    
    for inputs, expected in samples.items():
        result = logical_and(*inputs)
        print(f"logical_and({inputs[0]}, {inputs[1]}) = {result}, Expected: {expected}")