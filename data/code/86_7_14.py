if __name__ == '__main__':
    bool_pairs = {
        (True, True): False,
        (False, False): False,
        (True, False): True,
        (False, True): True
    }
    
    for (a, b), expected in bool_pairs.items():
        result = a == b
        print(f"Comparing {a} and {b}: {result}, Expected: {expected}")