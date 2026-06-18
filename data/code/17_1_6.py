def is_even(n: int) -> bool:
    """Check if an integer is even using the modulo operator."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [1, -5, 42, 0, 99]
    
    for num in samples:
        result = is_even(num)
        print(f"{num} is {'even' if result else 'odd'}")