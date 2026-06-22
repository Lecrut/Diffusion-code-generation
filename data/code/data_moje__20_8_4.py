def is_even(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer")
    return n % 2 == 0

def main():
    test_values = [0, 1, -1, 2, -2, 3, -3, 100, -100, 99, -99]
    for value in test_values:
        print(f"Input: {value}, Even: {is_even(value)}")

if __name__ == '__main__':
    main()