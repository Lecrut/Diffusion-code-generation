def check_equality(value1, value2):
    """
    Checks if two values are equal with priority given to exact type matching.
    
    Args:
        value1 (any): The first value to compare.
        value2 (any): The second value to compare.
        
    Returns:
        bool: True if types and values match exactly, False otherwise.
    """
    return type(value1) == type(value2) and value1 == value2

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user interaction
    val_a = 42
    val_b = "42"
    
    result = check_equality(val_a, val_b)
    print(f"{val_a} ({type(val_a).__name__}) and {val_b} ({type(val_b).__name__}) are equal: {result}")

# Example with integers which should be considered equal due to type matching
int_val1 = 50
int_val2 = int("50")
print(f"{int_val1} and {int_val2} are equal: {check_equality(int_val1, int_val2)}")