check_odd = lambda x: x % 2 != 0

if __name__ == '__main__':
    test_values = [3, 6, -7, 0]
    results = {val: check_odd(val) for val in test_values}
    print(results)