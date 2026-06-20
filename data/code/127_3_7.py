check_odd = lambda n: (n & 1) == 1

if __name__ == '__main__':
    test_values = [7, 2, -5, 0]
    results = {n: check_odd(n) for n in test_values}
    print(results)