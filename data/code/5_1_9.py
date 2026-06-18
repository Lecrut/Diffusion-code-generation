def compare_lengths(a: float, b: float) -> tuple[str, str]:
    """
    Compares two floating-point numbers and returns a tuple indicating 
    which length is greater or less (or if they are equal).
    
    Returns:
        A tuple of three strings based on the comparison result.
        - ("greater", "less") if a > b
        - ("equal", "") if a == b
        - ("less", "greater") if a < b
    
    This implementation uses direct comparison operators for efficiency and clarity.
    """
    if a > b:
        return ("greater", "less")
    elif a < b:
        return ("less", "greater")
    else:
        return ("equal", "")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 3.14
    val2 = 2.71
    
    result = compare_lengths(val1, val2)
    
    print(f"Comparing {val1} and {val2}:")
    if "greater" in result[0]:
        print(result[0], "> ", result[1])
    elif "equal" in result[0]:
        print("Equal", end="")
    else:
        print(f"{result[0]} < {result[1]}")