def compare_lengths(a: float, b: float) -> tuple[int]:
    """
    Compares two floating-point numbers and returns a tuple indicating their relationship.
    
    Args:
        a (float): First number to compare.
        b (float): Second number to compare.
        
    Returns:
        tuple[int]: A tuple where the first element is 1 if a > b, 
                    -1 if a < b, and 0 if they are equal.
    
    Note: This function uses direct comparison operators as requested.
          It does not perform any input validation beyond type checking at runtime.
    """
    if a > b:
        return (1,)
    elif a < b:
        return (-1,)
    else:
        return (0,)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    val_a = 3.5
    val_b = 2.7
    
    result = compare_lengths(val_a, val_b)
    
    print(f"Comparing {val_a} and {val_b}:")
    if result[0] == 1:
        print("First length is greater.")
    elif result[0] == -1:
        print("Second length is greater.")
    else:
        print("Lengths are equal.")