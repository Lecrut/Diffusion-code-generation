def compare_temperatures(temp1: float, temp2: float) -> tuple[str, str]:
    """
    Compares two floating-point temperature values.
    
    Returns a tuple (higher_val_str, relation_desc):
        - If temperatures are equal: ("equal", "both")
        - Otherwise: the string representation of the higher value and its relation to the lower one
    
    Args:
        temp1: First temperature in degrees Celsius or Fahrenheit.
        temp2: Second temperature in degrees Celsius or Fahrenheit.
    
    Returns:
        A tuple containing two strings describing which is higher/lower/equal.
    """
    if temp1 == temp2:
        return ("equal", "both")

    # Determine the maximum value directly using comparison operators
    max_val = temp1 if temp1 > temp2 else temp2
    
    if temp1 > temp2:
        relation_desc = f"{temp1} is higher than {temp2}"
    elif temp2 > temp1:
        relation_desc = f"{max_val} ({temp2}) is higher than {min(temp1, temp2)}"
    
    return (str(max_val), relation_desc)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a: float = 36.5
    t_b: float = 40.1
    
    result_higher, result_relation = compare_temperatures(t_a, t_b)
    
    print(f"Comparing {t_a}°C and {t_b}°C")
    print(f"Highest temperature is: {result_higher}")
    print(f"Relation description: {result_relation}")

    # Additional test case for equality
    result_equal = compare_temperatures(25.0, 25.0)
    print("\nTest Case (Equality):")
    print(result_equal[1])