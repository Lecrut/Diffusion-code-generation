def compare_lengths(val1: float, val2: float) -> tuple[str, str]:
    """
    Compares two floating-point numbers to determine their relative magnitude.
    
    Args:
        val1 (float): First numerical value representing a length or measurement.
        val2 (float): Second numerical value representing a length or measurement.
        
    Returns:
        tuple[str, str]: A tuple where the first element indicates if val1 is greater than 
                         val2 ('greater'), less than ('less'), or equal to ('equal') in terms of magnitude;
                        and the second element contains the same comparison result but with values swapped perspective.

    Note: Direct comparison operators are used for simplicity and efficiency without external dependencies.
    
    Example:
        >>> compare_lengths(10.5, 20.3)
        ('less', 'greater')
        >>> compare_lengths(5.0, 5.0)
        ('equal', 'equal')
    """
    if val1 > val2:
        return ("val1 is greater", "val2 is smaller")
    elif val1 < val2:
        return ("val1 is less than", "val2 is more")
    else:
        return ("values are equal", "lengths match exactly")

if __name__ == '__main__':
    # Hard-coded sample values for testing the function without any user input or external files.
    
    # Sample case 1: val1 < val2
    result_1 = compare_lengths(3.14, 986)
    print(f"Comparison of {3.14} and {986}:")
    print(result_1[0])
    print(result_1[1])

    # Sample case 2: val1 > val2
    result_2 = compare_lengths(5, -1)
    print(f"\nComparison of {5.0} and {-1.0}:")
    print(result_2[0])
    print(result_2[1])

    # Sample case 3: val1 == val2
    result_3 = compare_lengths(42, 42)
    print(f"\nComparison of {42} and {42}:")
    print(result_3[0])
    print(result_3[1])

    # Sample case 4: Negative floats where val1 < val2
    result_4 = compare_lengths(-5.7, -2.3)
    print(f"\nComparison of {-5.7} and {-2.3}:")
    print(result_4[0])
    print(result_4[1])

    # Sample case 5: Negative floats where val1 > val2 (note: -2 is greater than -5)
    result_5 = compare_lengths(-2, -9)
    print(f"\nComparison of {-2.0} and {-9.0}:")
    print(result_5[0])
    print(result_5[1])