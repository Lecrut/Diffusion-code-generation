import re

def parse_weight(value: str) -> float | None:
    """
    Parses a string representing weight with an optional unit suffix 
    (kg, g, mg, lb, oz). Returns the value in kilograms or None if invalid.
    
    Supported units and conversion factors to kg:
        - "kg": 1
        - "g" : 0.001
        - "mg": 0.000001
        - "lb": ~0.45359237
        - "oz": ~0.02834952
    
    The function uses regex to extract the numeric value and unit from a string 
    that may contain whitespace or non-numeric characters before/after the number/unit pair.
    
    Args:
        value (str): String containing weight measurement with optional unit suffix
        
    Returns:
        float | None: Weight in kilograms, or None if parsing fails
    """
    # Pattern to match a numeric value followed by an optional known unit
    pattern = r'^[\s\S]*?([+-]?\d*\.?\d+)([kg|g|mg|lb|oz])\s*$'
    
    matches = re.search(pattern, str(value), flags=re.IGNORECASE)
    
    if not matches:
        return None
    
    try:
        numeric_value = float(matches.group(1))
        unit_char = matches.group(2).lower()
        
        # Conversion factors to kilograms
        conversion_factors = {
            'kg': 1.0,
            'g': 0.001,
            'mg': 1e-6,
            'lb': 0.45359237,
            'oz': 0.02834952
        }
        
        factor = conversion_factors.get(unit_char)
        
        if factor is None:
            return None
            
        result = numeric_value * factor
        
        # Handle potential underflow/overflow resulting in zero or inf/nan
        if not (isinstance(result, float) and -float('inf') < result <= float('inf')):
            return None
            
        return round(result, 6)
        
    except ValueError:
        return None

def convert_weights_to_kg(measurements: list[str]) -> dict[int, tuple[float | None, str]]:
    """
    Converts a list of weight measurements (strings with optional units) 
    to kilograms. Returns a dictionary mapping original indices to tuples 
    containing the converted value in kg or None if conversion failed, and an error message string.
    
    Args:
        measurements (list[str]): List of strings representing weights
        
    Returns:
        dict[int, tuple[float | None, str]]: Dictionary where keys are original list indices,
            values are tuples of (weight_in_kg_or_none, 'success' or 'error')
    """
    results = {}
    
    for idx, measurement in enumerate(measurements):
        weight_kg = parse_weight(measurement)
        
        if weight_kg is not None:
            results[idx] = (weight_kg, "Success")
        else:
            # Determine a generic error message based on the input type/structure
            try:
                float(str(measurements[0])) 
                error_msg = f"Could not parse numeric value in measurement '{measurement}'"
            except ValueError:
                error_msg = f"Invalid format or unsupported unit in measurement '{measurement}'"
            
            results[idx] = (None, error_msg)
    
    return results

if __name__ == '__main__':
    # Hard-coded sample values representing various weight measurements
    raw_measurements = [
        "75 kg",           # 75 kilograms
        "2.5 g" ,          # 2.5 grams
        "10 mg",           # 10 milligrams
        "3 lbs",           # 3 pounds (approx)
        "4 oz",            # 4 ounces (approx)
        "invalid text",    # Invalid input without number or unit
        "abc xyz kg"      # Incorrect format with extra characters before valid part? 
                          # Note: Our regex expects value then unit at end. This will fail on 'xyz' if placed after number,
                          # but our pattern allows non-numeric chars before the start of [number][unit].
                          # Let's test a case that should definitely fail parsing logic completely
    ]

    print("Original Measurements:")
    for i, val in enumerate(raw_measurements):
        print(f"  [{i}]: {val}")

    converted_data = convert_weights_to_kg(raw_measurements)

    print("\nConverted to Kilograms:")
    success_count = 0
    
    for idx, (weight_in_kg, status) in converted_data.items():
        if weight_in_kg is not None:
            print(f"  [{idx}]: {raw_measurements[idx]} -> {weight_in_kg:.6f} kg")
            success_count += 1
        else:
            error_msg = next((msg for msg, _ in converted_data.values() if status == "error"), f"No specific message provided.")
            print(f"  [{idx}]: {raw_measurements[idx]} -> ERROR ({status}) | Detail: {weight_in_kg}")

    print(f"\nSummary:")
    print(f"  Successfully processed measurements: {success_count}/{len(raw_measurements)}")