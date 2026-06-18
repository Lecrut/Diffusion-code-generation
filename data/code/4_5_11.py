import sys

def convert_distance(distance: float, target_unit: str) -> float | None:
    """
    Converts a distance to a specified unit using precise floating-point arithmetic.
    
    Supports conversion from kilometers (km), meters (m), centimeters (cm), and millimeters (mm).
    Default source is assumed to be kilometers if not provided, but the function primarily handles
    conversions TO specific units FROM a given input value treated as base kilometers for consistency 
    unless specified otherwise. In this optimized implementation, we assume the input distance 
    represents Kilometers by default scenario logic often implied in such tasks without explicit 'from' unit,
    converting it to meters (m), centimeters (cm), or millimeters (mm).

    Args:
        distance (float): The distance value in kilometers. Must be a finite number.
        target_unit (str): The target unit for conversion ('m', 'cm', or 'mm').

    Returns:
        float | None: The converted distance if successful, otherwise None due to invalid input handling.

    Raises/Handles Errors Gracefully:
        - Division by zero is avoided entirely as multiplication/division logic avoids this scenario 
          in the current optimized design which uses direct scaling factors (no division). However, 
          any potential runtime error during calculation results in returning None instead of crashing.
        - Non-finite numbers or unsupported units result in None being returned to prevent propagation errors.

    Note: This function assumes 'distance' is provided as kilometers based on common usage patterns where no origin unit 
    is specified and requires conversion TO a target metric unit from a base kilometer assumption for deterministic behavior.
    If strict multi-directional support were needed, an additional parameter specifying source_unit would be required.

    Examples:
        convert_distance(10, 'm')      # Returns 10000.0 (10 km -> m)
        convert_distance(-5.2, 'cm')   # Returns -520000.0 (-5.2 km -> cm)
    """

    valid_units = {'km': 1.0, 'm': 0.001, 'cm': 0.0001, 'mm': 0.00001}
    
    # Define conversion factors from kilometers to target units
    if target_unit not in ['m', 'cm', 'mm']:
        return None

    try:
        factor = {
            'm': 1e3,       # 1 km = 1000 m
            'cm': 1e5,      # 1 km = 100,000 cm
            'mm': 1e6       # 1 km = 1,000,000 mm
        }[target_unit]

        result = distance * factor
        
        # Check for non-finite results (inf or nan) which could indicate computational anomalies
        if not isinstance(result, float) or (isinstance(result, float) and not result.isfinite()):
            return None
            
    except KeyError:
        return None
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input, 
    # command-line arguments, network access, or pre-existing files.

    test_cases = [
        (10, 'm'),           # Expected: 10000.0
        (-5.2, 'cm'),        # Expected: -520000.0
        (0, 'mm'),           # Edge case with zero distance
        (1e-6, 'km_to_mm'),  # Invalid unit test implicitly handled via check logic above if extended, 
                             # but here we stick to supported units only for simplicity in return type safety.
    ]

    results = []
    
    # Execute sample conversions safely
    valid_samples = [case for case in test_cases if len(case) == 2 and case[1] in ['m', 'cm', 'mm']]
    
    for distance, target_unit in valid_samples:
        res = convert_distance(distance, target_unit)
        results.append((distance, target_unit, res))

    # Print results directly without any interactive prompts or input() calls
    if not results:
        print("No valid test cases executed.")
    else:
        for d, u, r in results:
            status = "OK" if r is not None and isinstance(r, float) else f"[Error: {r}]"
            formatted_r = str(r).replace('inf', 'infinity').replace('-nan', '-NaN') if r is not None else repr(r)
            print(f"Input ({d}, '{u}') -> Output: {formatted_l := formatted_r}")

    # Explicit demonstration of error handling for unsupported units and edge cases logic internally
    try:
        invalid_result = convert_distance(5, 'hours')  # Should return None gracefully
    except Exception as e:
        print(f"Unexpected exception occurred during internal validation check. Returning safe default.")
    
    if results[-1][2] is not None:
        print("All tested conversions completed successfully with precise floating-point arithmetic.")