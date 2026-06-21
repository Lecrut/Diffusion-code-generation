def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [-4, -1, 0, 1, 2, 100, 101]
    for value in test_values:
        result = is_even(value)
        print(result)