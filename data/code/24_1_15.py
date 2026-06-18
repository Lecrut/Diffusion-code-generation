def is_negative(value):
    """
    Returns True if value is less than zero, False otherwise.
    
    Args:
        value (number): A numerical input.
        
    Returns:
        bool: True if value < 0, else False.
    """
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [-5, -1.5, 0, 3.7]
    
    for num in samples:
        result = is_negative(num)
        print(f"is_negative({num}) = {result}")