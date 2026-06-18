def compare_values(val1, val2):
    """
    Compares two values to check if they are equal.
    
    Args:
        val1 (any): The first value to compare.
        val2 (any): The second value to compare.
        
    Returns:
        bool: True if the values are equal, False otherwise.
    """
    try:
        return val1 == val2
    except TypeError as e:
        # Handle cases where types cannot be compared directly
        print(f"Error: Cannot compare these two inputs - {e}")
        return None

def main():
    # Hard-coded sample values for testing without user input
    value_a = 50
    value_b = "50"
    
    result = compare_values(value_a, value_b)
    
    if result is True:
        print(f"The inputs {value_a} and {value_b} are equal.")
    elif result is False:
        print(f"The inputs {value_a} and {value_b} are not equal.")
    else:
        print("The comparison failed due to incompatible types.")

if __name__ == '__main__':
    main()