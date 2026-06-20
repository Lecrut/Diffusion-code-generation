def logical_and(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    results = {
        (True, True): True,
        (True, False): False,
        (False, True): False,
        (False, False): False
    }
    
    for inputs, expected in results.items():
        result = logical_and(*inputs)
        print(f"{inputs} -> {result}, Expected: {expected}")