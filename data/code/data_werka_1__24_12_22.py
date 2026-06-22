def check_negativity(num):
    return num < 0

if __name__ == '__main__':
    test_values = [10, -5, 0.0, -3.14, 200]
    results = {value: check_negativity(value) for value in test_values}
    print(results)