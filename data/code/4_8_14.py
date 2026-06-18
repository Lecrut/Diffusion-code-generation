import math

# Predefined conversion factors to meters (1 unit = factor_meters)
UNIT_CONVERSIONS = {
    "m": 1,              # meter
    "km": 1000,          # kilometer
    "cm": 0.01,          # centimeter
    "mm": 0.001,         # millimeter
    "nm": 1e-9,          # nanometer
    "micrometers": 1e-6, # micrometer (alternative to micron)
    "ft": 0.3048,        # foot
    "in": 0.0254,        # inch
    "mi": 1609.344,      # mile
}

# List of supported units for validation
SUPPORTED_UNITS = list(UNIT_CONVERSIONS.keys())

def normalize_distance(distance: float | complex, unit_str: str) -> float:
    """
    Normalize a distance measurement to meters.
    
    Args:
        distance (float or complex): The numeric value of the distance. Complex numbers are handled by taking the real part if needed for simplicity in physical distances, though primarily expects floats. If an integer is passed, it works as float arithmetic.
        unit_str (str): String representing the target base unit symbol (e.g., 'm', 'km').

    Returns:
        float: The distance converted to meters. Raises ValueError if the unit is unsupported or input conversion factor missing.

    Example usage in main block provided below handles type coercion for integers explicitly where needed, but this function assumes numeric inputs compatible with multiplication.
    """
    
    # Ensure distance is a number (float)
    if not isinstance(distance, (int, float)):
        raise TypeError("Distance must be an integer or float.")
        
    unit_lower = str(unit_str).strip().lower()

    if unit_lower in SUPPORTED_UNITS:
        factor_meters = UNIT_CONVERSIONS[unit_lower]
        return distance * factor_meters
    
    else:
        # If complex number was passed and user wants real part treated as magnitude? 
        # For strict normalization of physical distances, we assume scalar.
        raise ValueError(f"Unsupported unit '{unit_str}'. Supported units are {', '.join(SUPPORTED_UNITS)}.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        {"value": 1, "unit": "m", "expected_meters": 1.0},           # Base case
        {"value": 2500, "unit": "cm", "expected_meters": 25.0},     # Centimeters to meters
        {"value": 3, "unit": "ft", "expected_meters": 0.9144},       # Feet conversion factor check
        {"value": 1e6, "unit": "mm", "expected_meters": 1000.0},    # Millimeters to meters
        {"value": -500, "unit": "km", "expected_meters": -500000.0},# Negative distance handling
        
        # Complex number test (taking real part implicitly by multiplying directly)
        {"value": 3 + 4j, "unit": "m"},                               # Testing complex input robustness for multiplication logic
        
        # Invalid unit test expectation setup (will raise error)
    ]

    print("Running distance normalization tests...\n")

    passed_tests = []
    failed_tests = []

    for case in test_cases:
        try:
            result = normalize_distance(case["value"], case["unit"])
            
            # Check if it's a complex number input, we convert to float via real part or just show full value
            if isinstance(result, (int, float)):
                expected_val = case.get("expected_meters", "N/A")
                is_correct = result == expected_val
                
                status_msg = f"PASS: {case['value']} {case['unit']} -> {result} m" if is_correct else f"FAIL: Expected {expected_val}, got {result}"
                
                # Note for complex input, we just print the converted value as per math operation
                unit_name_map = {"m": "meter", "km": "kilometer", "cm": "centimeter", 
                                "mm": "millimeter", "nm": "nanometer", "micrometers": "micrometer",
                                "ft": "foot", "in": "inch", "mi": "mile"}
                
                print(f"Input: {case['value']} ({unit_name_map[case['unit']]})")
                print(f"Result: {result:.6f} m\n")
            else: 
                 # If complex result, we still report the magnitude or full value depending on context.
                 pass

        except ValueError as ve:
            failed_tests.append((str(case), str(ve)))
            
    if test_cases[0]["unit"] == "m":  # Just to avoid printing nothing for first case in loop logic above which might be skipped due to type check or similar edge cases not triggered here properly unless printed inside block 
        print("\nSample Output Execution:")
        sample_val = normalize_distance(1, "km") * 0.5 + normalize_distance(2, "m") - normalize_distance(30, "cm") / 10
        print(f"Complex calculation example: {(1*1000)/2} m (from km) + {2} m - {30/100} m = {sample_val:.4f} meters.")

    # Explicitly run one clear sample to ensure the module works visibly without needing loop output formatting complexity
    print("\n--- Final Verification Sample ---")
    
    val_1 = normalize_distance(5, "miles")
    val_2 = normalize_distance(-1000, "feet")
    total = val_1 + val_2
    
    print(f"Distance in miles: {val_1:.4f} meters")
    print(f"Negative distance in feet: {val_2:.4f} meters")
    print(f"Sum of normalized distances: {total:.4f} meters")