def is_even(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return number % 2 == 0

if __name__ == "__main__":
    test_values = [-4, -2, -1, 0, 1, 2, 3]
    results = [is_even(n) for n in test_values]
    print(results)