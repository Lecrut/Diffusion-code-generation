def is_even(number: int) -> bool:
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [-2, -1, 0, 1, 2, 10, 11]
    results = [is_even(val) for val in test_values]
    for val, result in zip(test_values, results):
        print(f"is_even({val}) = {result}")