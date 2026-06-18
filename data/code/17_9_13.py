def is_even(n: int) -> bool:
    """Check if an integer is even."""
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [1, 2, -3, 4, 100]
    for num in sample_values:
        result = "even" if is_even(num) else "odd"
        print(f"{num} is {result}")