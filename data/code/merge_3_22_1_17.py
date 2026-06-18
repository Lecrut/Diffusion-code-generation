def is_odd(n):
    """Check if a number is odd using the modulo operator."""
    return n % 2 == 1

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [0, 1, -3, 42, -5]
    
    for num in samples:
        result = is_odd(num)
        print(f"Is {num} odd? {result}")