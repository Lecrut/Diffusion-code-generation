def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [10, -3, 0, 7, -8]
    results = {value: is_even(value) for value in test_values}
    print(results)