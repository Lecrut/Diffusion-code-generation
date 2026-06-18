def compare_floats(num1: float, num2: float) -> str:
    """
    Compares two floating-point numbers using a small epsilon to handle inaccuracies.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
        
    Returns:
        str: A string indicating which number is larger ('num1', 'num2', or 'equal').
    """
    # Define a tolerance for floating-point comparison (epsilon)
    EPSILON = 1e-9
    
    diff = num1 - num2
    
    if abs(diff) < EPSILON:
        return "equal"
    elif diff > 0:
        return "num1"
    else:
        return "num2"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    val_a = 3.5
    val_b = 4.7
    
    result = compare_floats(val_a, val_b)
    
    if result == "equal":
        print(f"{val_a} and {val_b} are equal")
    elif result == "num1":
        print(f"{val_a} is larger than {val_b}")
    else:
        print(f"{val_b} is larger than {val_a}")