import math

# Conversion factors relative to meters (1 meter = 0.000621371 miles, etc.)
CONVERSION_FACTORS = {
    "miles": 0.000621371,   # 1 mile in meters is approx 1/this? No, let's define as: value_in_meters * factor -> other_unit_value
}

# Let's redefine for clarity: To convert FROM unit TO meter: multiply by FACTOR_TO_METERS
FACTORS_TO_METERS = {
    "miles": 1609.344,      # 1 mile in meters
    "kilometers": 1000.0,   # 1 kilometer in meters
    "meters": 1.0           # 1 meter in meters
}

# To convert FROM unit TO any other unit: (value * FACTORS_TO_METERS[from]) / FACTORS_TO_METERS[to]

class DistanceConverter:
    def __init__(self):
        """Initialize the distance converter with internal conversion factors."""
        pass

    @staticmethod
    def _validate_unit(unit_str):
        """Validate if the provided unit string is supported."""
        valid_units = list(FACTORS_TO_METERS.keys())
        return unit_str.lower() in valid_units and isinstance(unit_str, str)

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a distance value from one unit to another.
        
        Args:
            value (float): The numeric distance value.
            from_unit (str): Source unit ('miles', 'kilometers', or 'meters').
            to_unit (str): Target unit ('miles', 'kilometers', or 'meters').

        Returns:
            float: Converted distance in the target unit.

        Raises:
            ValueError: If units are invalid, from/to is None/empty, value < 0.
            TypeError: If inputs are not of expected types (int/float).
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Distance value must be a number.")

        # Ensure non-negative distance as per physical logic for this task context
        if value < 0:
            raise ValueError(f"Negative distances are invalid. Provided: {value}")

        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if not DistanceConverter._validate_unit(from_unit) or not DistanceConverter._validate_unit(to_unit):
            valid_units_str = ", ".join(FACTORS_TO_METERS.keys())
            raise ValueError(f"Unsupported units. Valid options: {valid_units_str}")

        # Conversion logic via meters as intermediate unit for flexibility and readability
        value_in_meters = value * FACTORS_TO_METERS[from_unit]
        converted_value = value_in_meters / FACTORS_TO_METERS[to_unit]

        return float(converted_value)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    
    converter = DistanceConverter()
    
    print("Distance Converter Test Suite")
    print("-" * 30)
    
    test_cases = [
        {"value": 1, "from_unit": "miles", "to_unit": "kilometers"}, # Expected ~ 1.609
        {"value": 5, "from_unit": "kilometers", "to_unit": "meters"},   # Expected: 5000.0
        {"value": 2000, "from_unit": "meters", "to_unit": "feet"},     # Note: 'feet' not in constants? Will fail gracefully if strictly adhering to prompt constraints or handle error. 
                                # The task says: convert between ANY pair of SPECIFIED units (miles, kilometers, meters).
                                # So feet is NOT a valid unit per the instruction "any pair...".
        {"value": 10, "from_unit": "kilometers", "to_unit": "meters"},   # Expected: 10000.0
    ]

    # Adjusting test case to strictly follow constraints (only miles/kilometers/meters)
    corrected_test_cases = [
        {"value": 5, "from_unit": "kilometers", "to_unit": "miles"},       # ~3.1068
        {"value": 2.5, "from_unit": "kilometers", "to_unit": "meters"},    # 2500.0
        {"value": 100, "from_unit": "miles", "to_unit": "feet"}            # Let's skip this as 'feet' is not in the allowed list (miles/kilometers/meters) per prompt instructions.
    ]

    # Re-defining test cases strictly within m/k/M to avoid runtime errors on invalid units based on prompt constraints
    final_tests = [
        ("1 mile", "kilometers"),       # 0.621371 km
        (5, "miles", "km"),             # ~3.1 mi -> wait input is value + from/to
    
    ]

    results = []
    
    try: 
        result1 = converter.convert(1, "miles", "kilometers")
        print(f"Converting 1 mile to kilometers: {result1:.5f}")
        
        result2 = converter.convert(3.106856, "miles", "kilometers") # Reverse check roughly
        # Actually let's do simple direct conversions
        
    except Exception as e: 
        print(f"Error during conversion: {e}")

    # Explicit tests using the defined constants only (miles, kilometers, meters)
    
    test_data = [
        {"input": 1.0, "from": "miles", "to": "kilometers"},
        {"input": 5.0, "from": "kilo" + "meters".lower(), # Oops typo in thought process, use 'kilometers' 
         "to": "km"}],

    print("\nExecuting predefined tests:")
    
    test_set = [
        (1.0, "miles", "kilometers"),
        (5.0, "kilometers", "meters"),
        (2000.0, "meters", "feet") # INVALID UNIT per prompt constraints? Prompt says: miles/kilometers/meters only. 
    ]

    # Re-reading task carefully: "convert distances between any pair of specified units (miles, kilometers, meters)"
    # This implies the ONLY supported units are these three. 'feet' is NOT allowed in input validation unless I add it to constants? No, prompt says "specified units". 
    # So I will strictly enforce only m/k/M.

    print("\n--- Validated Test Cases (miles, kilometers, meters) ---")
    
    cases = [
        ("Convert 1 mile to km", lambda: converter.convert(1, "miles", "kilometers")),
        ("Convert 5000 meters to miles", lambda: converter.convert(5000, "meters", "miles")),
        ("Convert 2.6 kilometers to meters", lambda: converter.convert(2.6, "kilometers", "meters"))
    ]

    for desc in cases: 
        try:
            res = desc[1]()
            print(f"{desc[0]} -> {res}")
        except Exception as e:
            print(f"Failed: {e}")