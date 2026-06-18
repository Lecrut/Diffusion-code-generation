def analyze_temperatures(temp_a: float, temp_b: float) -> dict:
    """
    Analyzes two temperature inputs to determine their difference 
    and relative magnitude.
    
    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.
        
    Returns:
        dict: A dictionary containing the absolute difference, 
              whether a is greater than b, equal, or less than b.
    """
    diff = abs(temp_a - temp_b)
    
    if temp_a > temp_b:
        relation = "a is hotter"
    elif temp_a < temp_b:
        relation = "b is hotter"
    else:
        relation = "temperatures are equal"
        
    return {
        'difference': diff,
        'relation': relation
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    temp1 = 25.0
    temp2 = -3.5
    
    result = analyze_temperatures(temp1, temp2)
    
    print(f"Temperature Difference: {result['difference']}")
    print(f"Relative Magnitude: {result['relation']}")