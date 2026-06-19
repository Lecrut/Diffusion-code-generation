def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [0, -1, -2, 1, 2, 3, 4, 5]
    results = {n: is_even(n) for n in test_values}
    print(results)