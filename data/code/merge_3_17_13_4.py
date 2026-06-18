def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [1, 2, -3, 4]
    results = []
    for val in test_values:
        result = is_even(val)
        print(f"{val}: {result}")