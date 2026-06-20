check_odd = lambda n: n % 2 != 0

if __name__ == '__main__':
    test_values = [3, 4, 7, -1]
    results = {n: check_odd(n) for n in test_values}
    print(results)