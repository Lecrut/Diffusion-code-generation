def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
    even_results = {value: is_even(value) for value in test_values}
    print(even_results)