def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == "__main__":
    test_values = [0, 1, 2, 3, 4, 10, 101, 1000]
    for value in test_values:
        print(is_even(value))