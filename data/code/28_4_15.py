def is_larger(a: float, b: float) -> bool:
    """
    Determine if number 'a' is strictly larger than number 'b'.
    
    This function uses a single built-in comparison operator to minimize 
    computational steps. It returns True if a > b, otherwise False.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if 'a' is larger than 'b', False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    test_values = [
        (10, 5),      # True case: 10 is larger than 5
        (3.14, 2.71),# True case: Pi is larger than approx e's first digits sum
        (-5, -2),     # False case: negative five is not larger than negative two
        (0, 0),       # False case: zero is equal to itself
    ]

    for val_a, val_b in test_values:
        result = is_larger(val_a, val_b)
        print(f"is_larger({val_a}, {val_b}) -> {result}")