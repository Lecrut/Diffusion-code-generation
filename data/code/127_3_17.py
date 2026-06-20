check_odd = lambda n: (n & 1) == 1

if __name__ == '__main__':
    test_values = [5, 4, 0, -3, 7]
    results = {value: check_odd(value) for value in test_values}
    print(results)