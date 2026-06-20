if __name__ == '__main__':
    comparisons = {
        (True, True): True,
        (False, False): True,
        (True, False): False,
        (False, True): False
    }
    
    for (a, b), expected in comparisons.items():
        result = a == b
        print(f"Comparing {a} and {b}: {result}, Expected: {expected}")