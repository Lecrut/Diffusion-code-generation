def check_equality(value1: any, value2: any) -> bool:
    """Check if two values are equal."""
    try:
        return value1 == value2
    except TypeError as e:
        print(f"Error: Cannot compare these types. {e}")
        return False

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input
    val_a = 50
    val_b = "50"
    
    result = check_equality(val_a, val_b)
    if result:
        print("The two inputs are equal.")
    else:
        print("The two inputs are not equal.")