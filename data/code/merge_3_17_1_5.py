def is_even(number: int) -> bool:
    """Check if a number is even using the modulo operator."""
    return number % 2 == 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [1, -5, 42, 0, 3.7]  # Note: input must be int as per requirement
    
    for num in samples:
        try:
            result = is_even(num)
            print(f"{num} is {'even' if result else 'odd'}")
        except TypeError:
            print(f"Error with {type(num).__name__}: Input must be an integer.")