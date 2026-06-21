def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [-4, -1, 0, 2, 5]
    for value in test_values:
        print(is_even(value))