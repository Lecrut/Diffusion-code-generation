def is_odd(n: int) -> bool:
    """Check if an integer n is odd."""
    return n % 2 != 0

if __name__ == '__main__':
    # Hard-coded sample values to test the logic without user input.
    samples = [1, 2, -3, 4]

    for num in samples:
        if is_odd(num):
            print(f"{num} is odd.")
        else:
            print(f"{num} is even.")