def compare_lengths(a: float, b: float) -> tuple[int]:
    """
    Compare two floating-point numbers and return a status tuple.
    
    Args:
        a (float): First number to compare.
        b (float): Second number to compare.
        
    Returns:
        tuple[int]: A tuple of length 1 containing an integer code:
            - 0 if lengths are equal (a == b)
            - 1 if first is greater (a > b)
            - 2 if second is greater (b > a)
    """
    result = [0]
    
    # Direct comparison using operators to determine the relationship
    if a > b:
        result[0] = 1
    elif a < b:
        result[0] = 2
    
    return tuple(result)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val_a = 3.14159
    val_b = 2.71828
    
    status, code = compare_lengths(val_a, val_b)
    
    print(f"Comparing {val_a} and {val_b}")
    if status == 0:
        print("Lengths are equal")
    elif status == 1:
        print(f"{val_a} is greater than {val_b}")
    else:
        print(f"{val_b} is greater than {val_a}")