import sys

# Define conversion factors relative to meters (SI base unit)
CONVERSION_FACTORS = {
    "m": 1,           # meter
    "km": 0.001,      # kilometer
    "cm": 100,        # centimeter
    "mm": 1000,       # millimeter
    "mi": 1609.344,   # mile (international)
    "yd": 0.9144,     # yard
    "ft": 0.3048,     # foot
    "in": 0.0254,     # inch
}

# Supported units list for validation
SUPPORTED_UNITS = set(CONVERSION_FACTORS.keys())

def convert_distance(distance: float, from_unit: str, to_unit: str) -> dict:
    """
    Converts a distance value from one unit to another.
    
    Args:
        distance (float): The numerical value of the distance.
        from_unit (str): Source unit identifier (e.g., 'km', 'mi').
        to_unit (str): Target unit identifier (e.g., 'm', 'ft').

    Returns:
        dict: A dictionary containing status, original_value, converted_value, 
              and error_message if applicable.
    
    Raises:
        ValueError: If units are unsupported or distance is invalid.
    """
    result = {
        "status": "success",
        "original_distance": distance,
        "converted_distance": None,
        "error_message": None
    }

    # Validate input types and values
    if not isinstance(distance, (int, float)):
        raise ValueError("Distance must be a numeric value.")
    
    if from_unit.lower() not in SUPPORTED_UNITS or to_unit.lower() not in SUPPORTED_UNITS:
        result["status"] = "error"
        result["converted_distance"] = None
        result["error_message"] = f"Unsupported unit. Supported units are: {', '.join(sorted(SUPPORTED_UNITS))}"
        return result

    # Normalize unit identifiers to lowercase for consistency
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()

    try:
        factor_from = CONVERSION_FACTORS[from_unit_lower]
        factor_to = CONVERSION_FACTORS[to_unit_lower]

        # Convert to meters first, then to target unit
        distance_in_meters = distance * factor_from
        converted_distance = distance_in_meters / factor_to
        
        result["converted_distance"] = round(converted_distance, 6)
        
    except ZeroDivisionError:
        result["status"] = "error"
        result["converted_distance"] = None
        result["error_message"] = "Target unit conversion resulted in division by zero."

    return result

if __name__ == '__main__':
    # Hard-coded sample inputs to demonstrate functionality without user interaction
    
    test_cases = [
        {"distance": 1, "from_unit": "km", "to_unit": "m"},           # 1 km -> m
        {"distance": 5.28, "from_unit": "mi", "to_unit": "ft"},      # 1 mile in feet approx
        {"distance": 3600, "from_unit": "s", "to_unit": "h"},       # Note: 's' not supported, will test error handling below instead. 
        {"distance": 254, "from_unit": "in", "to_unit": "cm"},      # Exact conversion
    ]

    # Corrected sample case for unsupported unit demonstration
    invalid_case = {
        "distance": 10, 
        "from_unit": "miles_to_meters" if False else None, # Placeholder logic to force error check manually below
    }

    # Re-defining a specific test for the 's' (seconds) which is not in our list but simulates an invalid unit string passed as input
    # Actually, let's just run valid cases and one known-invalid case explicitly constructed.
    
    samples = [
        {"distance": 100, "from_unit": "km", "to_unit": "m"},         # Expected: 100000 m
        {"distance": 5280, "from_unit": "ft", "to_unit": "mi"},       # Expected: ~3.96 mi (wait, input is ft) -> 1 mile = 5280 ft? No. 
                        # Let's stick to simple math: 5280 ft * 0.3048 m/ft / 1609.344 m/mi
        {"distance": 75, "from_unit": "cm", "to_unit": "m"},         # Expected: 0.75 m
    ]

    print("=== Distance Unit Converter System ===")
    
    for i, sample in enumerate(samples):
        try:
            output = convert_distance(
                distance=sample["distance"], 
                from_unit=sample["from_unit"], 
                to_unit=sample["to_unit"]
            )
            
            print(f"\nTest Case {i+1}:")
            if output["status"] == "success":
                print(f"  Input:   {output['original_distance']} {sample['from_unit']}")
                print(f"Output:    {output['converted_distance']} {sample['to_unit']}")
            else:
                print(f"Error: {output['error_message']}")

        except ValueError as e:
            print(f"\nTest Case Error (Value): {e}")

    # Demonstrate error handling for unsupported unit explicitly without using input()
    invalid_sample = {"distance": 10, "from_unit": "invalid_x", "to_unit": "m"}
    
    try:
        result_invalid = convert_distance(
            distance=invalid_sample["distance"], 
            from_unit=invalid_sample["from_unit"], 
            to_unit=invalid_sample["to_unit"]
        )
        
        print("\nTest Case (Invalid Unit):")
        if result_invalid["status"] == "error":
            print(f"  Input:   {result_invalid['original_distance']} {invalid_sample['from_unit']} -> {invalid_sample['to_unit']}")
            print(f"Error Message: {result_invalid['error_message']}")
    except ValueError as e:
        print(f"\nUnexpected Error during invalid unit test: {e}")

    # Final demonstration of a complex conversion chain logic (km to inches)
    final_test = {"distance": 1, "from_unit": "km", "to_unit": "in"}
    
    try:
        result_final = convert_distance(
            distance=final_test["distance"], 
            from_unit=final_test["from_unit"], 
            to_unit=final_test["to_unit"]
        )
        
        print("\nFinal Test (1 km to inches):")
        if result_final["status"] == "success":
            print(f"  Input:   {result_final['original_distance']} {final_test['from_unit']}")
            print(f"Output:    {result_final['converted_distance']} {final_test['to_unit']}")
            
    except ValueError as e:
        print(f"\nUnexpected Error in final test: {e}")

    sys.exit(0)