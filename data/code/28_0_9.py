def is_larger(a: float, b: float) -> bool:
    """
    Returns True if a is strictly larger than b, False otherwise.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values; no user input or external dependencies required.
    result1 = is_larger(5.0, 3.0)
    print(f"is_larger(5.0, 3.0) = {result1}")

    result2 = is_larger(4.5, 4.5)
    print(f"is_larger(4.5, 4.5) = {result2}")

    result3 = is_larger(-1.0, -5.0)
    print(f"is_larger(-1.0, -5.0) = {result3}")