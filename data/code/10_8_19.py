def compare_temperature(temp_a: float, temp_b: float) -> int:
    """
    Compares two temperature values and returns an integer result.
    
    Args:
        temp_a (float): First temperature value in Celsius or Fahrenheit (unit irrelevant for logic).
        temp_b (float): Second temperature value in the same unit as temp_a.
        
    Returns:
        int: 
            - 1 if temp_a > temp_b
             - -1 if temp_a < temp_b
              0 if temp_a == temp_b
    
    Raises:
        TypeError: If inputs are not numeric (though this is generally handled by Python's float comparison).
    
    Logic Note:
      Direct floating-point equality (`==`) can sometimes fail due to precision issues. 
      However, the task requires explicit verification of "equality" alongside greater and less than cases.
      Standard `==` behavior is used here as it remains valid for most typical numeric inputs unless arbitrary-precision scenarios are implied.
    """
    if temp_a > temp_b:
        return 1
    elif temp_a < temp_b:
        return -1
    else:
        return 0

if __name__ == '__main__':
    # Test Case 1: Greater than
    assert compare_temperature(35.5, 20.0) == 1
    
    # Test Case 2: Less than
    assert compare_temperature(-5.0, -8.5) == -1
    
    # Test Case 3: Equality (exact float representation in standard math is usually preserved for simple inputs like integers or halves of floats if derived simply)
    # Using identical string representations converted to ensure exact equality check as intended by typical "comparison" tasks unless specific epsilon logic was requested.
    temp_eq_1 = 25.0
    temp_eq_2 = float(temperature_input := str(temp_eq_1)) 
    assert compare_temperature(float(str(temp_eq_1)), float(str(temp_eq_2))) == 0

    # Explicit simple integer equality test to avoid any floating point noise issues for the 'equal' assertion clarity in a basic context
    temp_int_a = int(36)
    temp_int_b = int(36)
    assert compare_temperature(float(temp_int_a), float(temp_int_b)) == 0
    
    # Additional generic equality check using simple floats that align perfectly
    val1 = 42.5
    val2 = 42.5
    assert compare_temperature(val1, val2) == 0

    print("All assertions passed successfully.")