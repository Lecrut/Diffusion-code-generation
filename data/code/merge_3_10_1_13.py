def compare_temperatures(temp1: float, temp2: float) -> tuple[str]:
    """
    Compares two floating-point temperature values.
    
    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.
        
    Returns:
        A tuple containing a single string indicating the result of comparison:
            - ('higher',) if temp1 > temp2
            - ('lower',)  if temp1 < temp2
            - ('equal',)  if temp1 == temp2
    """
    if temp1 > temp2:
        return ('higher',)
    elif temp1 < temp2:
        return ('lower',)
    else:
        return ('equal',)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (36.5, 40.0),   # First is lower
        (-10.2, -5.8), # First is higher
        (22.0, 22.0),  # Both are equal
        (0.0, 0.0000001), # Precision difference check
    ]

    for t_a, t_b in sample_cases:
        result = compare_temperatures(t_a, t_b)
        print(f"Comparing {t_a} and {t_b}: Result is '{result[0]}'")