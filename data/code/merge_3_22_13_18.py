def is_odd(num):
    return num % 2 != 0
    
if __name__ == '__main__':
    test_cases = [5, 4, -3, 0]
    results = []
    for n in test_cases:
        r = is_odd(n)
        print(f"is_odd({n}) = {r}")