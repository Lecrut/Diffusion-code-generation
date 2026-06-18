def is_larger(a: float, b: float) -> bool:
    """
    Determine if number 'a' is strictly larger than number 'b'.
    
    Uses Python's built-in comparison operator '>' which is implemented 
    in C and performs a single computational step. This avoids any manual 
    implementation logic that would require multiple steps (like subtraction).

    Args:
        a: The first numeric value to compare.
        b: The second numeric value to compare against 'a'.

    Returns:
        True if a > b, False otherwise.
    
    Example usage: is_larger(5, 3) returns True; is_larger(2, 7) returns False.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        (10, 5),      # Expected: True
        (-3, -6),     # Expected: True (negative numbers)
        (4.2, 4.2),   # Expected: False (equal values)
        (float('inf'), float('-inf')),  # Expected: True
    ]

    for val_a, val_b in samples:
        result = is_larger(val_a, val_b)
        print(f"is_larger({val_a}, {val_b}) => {result}")