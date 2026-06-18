def is_even(n: int) -> bool:
    """Check if an integer is even using the modulo operator."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [1, -5, 42, 0, 3.7]  # Note: only integers are expected by type hint
    
    for num in samples:
        if isinstance(num, int):
            result = is_even(num)
            print(f"is_even({num}) = {result}")
        else:
            print(f"Skipping non-integer input: {num}")