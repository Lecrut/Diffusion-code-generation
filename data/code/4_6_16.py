import sys

# Define conversion factors relative to meters (SI base unit)
CONVERSION_FACTORS = {
    "meter": 1,
    "kilometer": 0.001,
    "centimeter": 100,
    "millimeter": 1000,
    "mile": 0.000621371,
    "yard": 1.09361,
    "foot": 3.28084,
    "inch": 39.3701,
}

SUPPORTED_UNITS = list(CONVERSION_FACTORS.keys())

def convert_distance(distance: float, from_unit: str, to_unit: str) -> dict:
    """
    Converts a distance value between supported units with error handling.
    
    Args:
        distance (float): The numerical value of the distance.
        from_unit (str): Source unit string (case-insensitive).
        to_unit (str): Target unit string (case-insensitive).
        
    Returns:
        dict: A dictionary containing 'success' status, 'result', and 'message'.
    
    Raises:
        ValueError: If units are unsupported or input is invalid.
    """
    # Normalize inputs for case insensitivity
    from_unit_lower = from_unit.lower().strip()
    to_unit_lower = to_unit.lower().strip()

    # Validate distance type
    if not isinstance(distance, (int, float)):
        return {
            "success": False,
            "result": None,
            "message": f"Distance must be a number. Received: {type(distance).__name__}"
        }

    if distance < 0 or abs(distance) > 1e308: # Basic float check for negative and overflow safety
        return {
            "success": False,
            "result": None,
            "message": f"Invalid distance value. Must be non-negative."
        }

    # Validate source unit
    if from_unit_lower not in SUPPORTED_UNITS:
        valid_units = ", ".join(SUPPORTED_UNITS)
        return {
            "success": False,
            "result": None,
            "message": f"Unsupported source unit '{from_unit}'. Supported units are: {valid_units}"
        }

    # Validate target unit
    if to_unit_lower not in SUPPORTED_UNITS:
        valid_units = ", ".join(SUPPORTED_UNITS)
        return {
            "success": False,
            "result": None,
            "message": f"Unsupported target unit '{to_unit}'. Supported units are: {valid_units}"
        }

    # Perform conversion via meters (SI base)
    factor_from = CONVERSION_FACTORS[from_unit_lower]
    factor_to = CONVERSION_FACTORS[to_unit_lower]

    try:
        value_in_meters = distance * factor_from
        converted_value = value_in_meters / factor_to
        
        return {
            "success": True,
            "result": float(converted_value),
            "message": f"Converted {distance} {from_unit} to {to_unit}: {converted_value}"
        }
    except OverflowError:
        return {
            "success": False,
            "result": None,
            "message": "Conversion resulted in an overflow. Please try smaller values."
        }

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access
    
    test_cases = [
        {"distance": 10, "from_unit": "kilometer", "to_unit": "mile"},
        {"distance": 5280, "from_unit": "foot", "to_unit": "meter"},
        {"distance": 63.37, "from_unit": "inch", "to_unit": "centimeter"},
    ]

    print("Distance Conversion System")
    print("-" * 40)

    for i, case in enumerate(test_cases):
        result = convert_distance(
            distance=case["distance"], 
            from_unit=case["from_unit"], 
            to_unit=case["to_unit"]
        )

        if result["success"]:
            print(f"Test {i+1}:")
            print(f"  Input: {result['message']}")
            print()
        else:
            print(f"Test {i+1} Failed:")
            print(f"  Error: {result['message']}")
            print()

    # Additional edge case test for invalid unit
    error_case = convert_distance(5, "invalid_unit", "meter")
    if not error_case["success"]:
        print("Edge Case Test (Invalid Unit):")
        print(f"  Expected Error: {error_case['message']}")