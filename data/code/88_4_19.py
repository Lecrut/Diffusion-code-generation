def logical_and(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    results = {
        (True, True): True,
        (True, False): False,
        (False, True): False,
        (False, False): False
    }
    
    for (val1, val2), expected in results.items():
        result = logical_and(val1, val2)
        print(f"logical_and({val1}, {val2}) = {result}, Expected: {expected}")