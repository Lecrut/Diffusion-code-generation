def is_even(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return (n & 1) == 0

if __name__ == "__main__":
    sample_values = [4, 7, 0, -2, -5, 100]
    for value in sample_values:
        print(is_even(value))