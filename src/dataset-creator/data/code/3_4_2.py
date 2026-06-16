def is_even(n: int) -> bool:
    if not isinstance(n, (int, bool)):
        raise TypeError("Input must be an integer.")
    return n & 1 == 0
def main():
    test_cases = [42, -7, 0, 1, 8]
    for value in test_cases:
        result = is_even(value)
        print(f"Number {value} is {'even' if result else 'odd'}")
if __name__ == '__main__':
    main()