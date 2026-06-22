def is_even(number: int) -> bool:
    return True if number % 2 == 0 else False

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 10, 15, 0, -2, -3]
    results = [is_even(val) for val in test_values]
    for val, res in zip(test_values, results):
        print(f"{val}: {res}")