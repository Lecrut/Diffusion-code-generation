def is_positive(n):
    return n > 0

if __name__ == '__main__':
    test_values = [1, -2, 0, 3, -5]
    results = {value: is_positive(value) for value in test_values}
    print(results)