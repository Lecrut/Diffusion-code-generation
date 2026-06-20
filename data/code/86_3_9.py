def compare_booleans(a, b):
    return [a == b]

if __name__ == '__main__':
    comparisons = {
        (True, False): compare_booleans(True, False),
        (True, True): compare_booleans(True, True),
        (False, True): compare_booleans(False, True)
    }
    
    for sample, result in comparisons.items():
        print(f"Comparing {sample}: {result}")