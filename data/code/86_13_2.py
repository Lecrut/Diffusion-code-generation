def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    results = {
        (True, True): True,
        (False, False): True,
        (True, False): False
    }
    
    for inputs, expected in results.items():
        result = compare_booleans(*inputs)
        print(f"compare_booleans{inputs} -> {result}, Expected: {expected}")