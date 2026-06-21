def is_even(n):
    if n % 2 != 0:
        return False
    return True

if __name__ == '__main__':
    test_values = [15, 24, -9, 8, 0, -7, 12]
    results = {value: is_even(value) for value in test_values}
    print(results)