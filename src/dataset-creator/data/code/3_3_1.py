def is_even(n):
    if not isinstance(n, int) or n < 0:
        raise TypeError("Input must be a non-negative integer.")
    return n % 2 == 0
if __name__ == '__main__':
    test_values = [0, 1, 2, -5]
    for value in test_values:
        try:
            result = is_even(value)
            print(f"{value} is {'even' if result else 'odd'}")
        except TypeError as e:
            print(f"Error processing {value}: {e}")