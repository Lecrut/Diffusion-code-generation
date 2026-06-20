def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    comparisons = {
        (True, True): "True",
        (False, False): "False",
        (True, False): "False",
        (False, True): "False"
    }
    
    for (a, b), expected in comparisons.items():
        result = compare_booleans(a, b)
        print(f"Comparing {a} and {b}: {result}, Expected: {expected}")