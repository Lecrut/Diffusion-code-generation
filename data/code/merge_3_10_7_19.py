def analyze_temperature_difference(temp_a: float, temp_b: float) -> dict:
    """
    Analyzes two temperature inputs to determine their difference 
    and relative magnitude.

    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.

    Returns:
        dict: A dictionary containing the absolute difference, sign of difference,
              which is higher, and whether they are equal.
    """
    diff = abs(temp_a - temp_b)
    
    if temp_a > temp_b:
        magnitude_indicator = "A"
        direction_text = f"{temp_a} is {diff:.2f} units hotter than {temp_b}"
    elif temp_b > temp_a:
        magnitude_indicator = "B"
        direction_text = f"{temp_b} is {diff:.2f} units colder (hotter) than {temp_a}"
    else:
        magnitude_indicator = "="
        direction_text = "Both temperatures are equal."

    return {
        'absolute_difference': diff,
        'magnitude_indicator': magnitude_indicator,
        'description': direction_text
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    temp_sample_a = 25.0
    temp_sample_b = -10.5

    result = analyze_temperature_difference(temp_sample_a, temp_sample_b)
    
    print(f"Analysis of {temp_sample_a}°C and {temp_sample_b}°C:")
    print(result['description'])
    print(f"Difference: {result['absolute_difference']:.2f}")