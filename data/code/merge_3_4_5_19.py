import math

def convert_distance(distance: float, target_unit: str) -> dict:
    """
    Converts a distance value to the specified unit using precise floating-point arithmetic.
    
    Supported units (source): 'meters', 'kilometers', 'feet'
    Supported units (target): 'inches', 'centimeters', 'yards', 'miles'
    
    Handles potential division by zero errors gracefully and returns a status dictionary.
    
    Args:
        distance (float): The numerical value of the distance in meters (default base).
        target_unit (str): The unit to convert to. Must be one of: 'inches', 'centimeters', 
                          'yards', or 'miles'. If invalid, returns an error status.
    
    Returns:
        dict: A dictionary containing either the conversion result with keys 'success' and 'value',
              or an error message if division by zero occurs (though standard conversions are safe),
              or a validation failure key 'error' for unsupported units.
    """
    # Base unit is meters. Define precise conversion factors to base meters first,
    # then calculate the target factor relative to base to avoid intermediate rounding errors in logic flow,
    # though direct multiplication/division with standard floats provides sufficient precision here.
    
    valid_targets = {'inches', 'centimeters', 'yards', 'miles'}
    
    if not isinstance(distance, (int, float)) or distance == 0:
        return {"success": False, "error": "Distance must be a non-zero numeric value."}
    
    # Define conversion factors from meters to target units.
    # Using high-precision constants available in Python floats (double precision).
    if target_unit not in valid_targets:
        return {"success": False, "error": f"Unsupported unit '{target_unit}'. Valid units are {valid_targets}."}
    
    try:
        # Conversion factors from meters to the target unit.
        # 1 meter = 39.37007874 inches
        # 1 meter = 100 centimeters
        # 1 meter = 1.093613298 yards (approx) -> actually defined as exactly 1 yard / 0.9144 m, so factor is ~1/0.9144
        # 1 meter = 0.000621371 miles
        
        if target_unit == 'inches':
            factors = {'base_to_meters': 1.0, 'meters_to_target': 39.37007874}
        elif target_unit == 'centimeters':
            factors = {'base_to_meters': 1.0, 'meters_to_target': 100.0}
        elif target_unit == 'yards':
            # Exact definition: 1 yard = 0.9144 meters exactly
            factors = {'base_to_meters': 1.0 / 0.9144, 'meters_to_target': 1.0} 
        else: # miles
            # Standard approximation used in most contexts unless specified otherwise (statute mile)
            factors = {'base_to_meters': 1609.344, 'meters_to_target': 1/1609.344}
        
        result_value = distance * factors['meters_to_target'] / factors['base_to_meters']
        
    except ZeroDivisionError:
        return {"success": False, "error": "Internal calculation error: Division by zero occurred."}
    
    # Final check for NaN or Inf resulting from the operation (though input validation covers most cases)
    if not math.isfinite(result_value):
        return {"success": False, "error": "Result is not finite."}
        
    return {
        "success": True, 
        "value": result_value, 
        "unit": target_unit,
        "input_distance_meters": distance
    }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    samples = [
        {"distance": 100, "target_unit": "inches"},
        {"distance": 5.5, "target_unit": "miles"},
        {"distance": -20, "target_unit": "centimeters"}, # Negative distance test (should work mathematically)
        {"distance": 1609.344, "target_unit": "yards"},
    ]
    
    results = []
    for sample in samples:
        res = convert_distance(sample["distance"], sample["target_unit"])
        if "error" not in res or (res.get("success", False)):
            print(f"Input: {sample['distance']} meters -> {sample['target_unit']}: {res}")
        else:
            print(f"Error for input {sample}: {res}")