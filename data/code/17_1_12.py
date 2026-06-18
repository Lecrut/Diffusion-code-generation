def is_even(n: int) -> bool:
    """Check if an integer is even using the modulo operator."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [1, -5, 0, 42, 3.5]

    results = []
    for num in test_cases:
        if isinstance(num, int):
            result = is_even(num)
        else:
            # Non-integer input should be skipped or handled gracefully; 
            # here we only process integers as per the function signature requirement.
            continue
        
        results.append(f"Input {num} -> Even: {result}")

    for res in results:
        print(res)