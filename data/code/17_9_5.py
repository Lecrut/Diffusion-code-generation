def is_even(n: int) -> bool:
    """Check if an integer is even."""
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [1, 2, -3, 4, 5, 6]
    
    for num in sample_values:
        result = "Even" if is_even(num) else "Odd"
        print(f"{num}: {result}")