def check_evenness(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [-2, -1, 0, 1, 2]
    for val in test_values:
        result = check_evenness(val)
        print(result)