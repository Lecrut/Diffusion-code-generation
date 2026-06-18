def is_odd(n: int) -> bool:
    """Check if an integer is odd."""
    return n % 2 == 1

if __name__ == '__main__':
    num = 17
    result = is_odd(num)
    print(f"The number {num} {'is' if result else 'is not'} odd.")