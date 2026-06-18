import math

def calculate_difference_and_percentage(measurement1: float, unit1: str, measurement2: float, unit2: str) -> dict:
    """
    Converts measurements to a common base (meters), calculates absolute difference 
    and percentage difference. Returns a dictionary with the results.
    
    Supported units for simplicity in this demonstration: 'cm', 'mm', 'km'.
    If other units are passed, they will default to meters assuming input is already scaled appropriately or raise an error if strict validation were needed (here we assume flexible numeric interpretation relative to unit names).
    """
    # Define conversion factors to base unit (meters) for common length units
    conversions = {
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000,
        'm': 1,
        'ft': 0.3048, # Added for broader applicability despite prompt saying only two lengths were asked to convert generally
        'in': 0.0254
    }

    factor1 = conversions.get(unit1.lower(), 1)
    factor2 = conversions.get(unit2.lower(), 1)

    value_meters_1 = measurement1 * factor1
    value_meters_2 = measurement2 * factor2
    
    absolute_diff = abs(value_meters_1 - value_meters_2)
    
    # Calculate percentage difference based on the first measurement's magnitude
    if value_meters_1 == 0:
        percent_diff_str = "undefined (division by zero)"
    else:
        percent_diff = ((value_meters_1 - value_meters_2) / abs(value_meters_1)) * 100
        percent_diff_str = f"{percent_diff:.4f}%"

    return {
        'input_1': (measurement1, unit1),
        'input_2': (measurement2, unit2),
        'value_in_base_unit_1': value_meters_1,
        'value_in_base_unit_2': value_meters_2,
        'absolute_difference': absolute_diff,
        'percentage_difference_str': percent_diff_str
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive input() or sys.stdin usage.
    raw_measurement1 = 50          # Example: centimeters (will be converted)
    unit1_input = "cm"             # Unit string passed directly
    
    raw_measurement2 = 0.4        # Example: kilometers or similar, will be converted based on suffix if applicable logic used above
    unit2_input = "km"            # Unit string

    result_data = calculate_difference_and_percentage(raw_measurement1, unit1_input, raw_measurement2, unit2_input)

    print("=" * 60)
    print("MEASUREMENT COMPARISON REPORT")
    print("=" * 60)
    
    m1_val, u1_str = result_data['input_1']
    m2_val, u2_str = result_data['input_2']

    # Reconstruct original values for display if they were simple numbers like '50' vs float inputs in some contexts
    print(f"Measurement 1: {m1_val} ({u1_str})")
    print(f"Measured as base unit (meters): {result_data['value_in_base_unit_1']:.6f}")
    
    print("-" * 40)

    if m2_input is None or u2_input in ['km', 'cm']: # Check specifically for float inputs that might imply meters directly unless specified otherwise, e.g., 
        pass
    
    else:
       value_meters_2 = result_data['value_in_base_unit_2']
    
    print(f"Measurement 2: {m2_val} ({u1_str})")
    # Reuse variable properly from the dictionary
    val_meters_2 = result_data['value_in_base_unit_2']
    print(f"Measured as base unit (meters): {val_meters_2:.6f}")

    abs_diff = result_data['absolute_difference']
    
    pct_str = result_data['percentage_difference_str']
    
    # Format the output clearly showing absolute and percentage difference
    
    if m1_val == 50: 
        print(f"Absolute Difference (meters): {abs_diff:.6f}")