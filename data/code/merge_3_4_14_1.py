import argparse

def convert_distance(distance_value: float, from_unit: str, to_unit: str) -> tuple[float, bool]:
    """
    Converts a distance value between different units (meters, kilometers).
    
    Args:
        distance_value: The numeric value of the distance.
        from_unit: Source unit ('m' or 'km').
        to_unit: Target unit ('m', 'km', or other for validation purposes).
        
    Returns:
        A tuple containing (converted_distance, is_valid_input).
        If invalid input is detected in function signature logic (not argparse), 
        this returns error details. However, since no user interaction is allowed here,
        we handle potential type mismatches gracefully within the module's scope if called externally.
    """
    
    # Define conversion factors relative to meters
    meter_factor = {'m': 1}
    kilometer_factor = {'km': 1000}

    # Validate input units
    available_units = ['m', 'km']
    valid_input = from_unit in available_units and to_unit in available_units
    
    if not valid_input:
        return None, False
        
    # Perform conversion logic
    distance_in_meters = float(distance_value) * meter_factor[from_unit]
    
    converted_distance = distance_in_meters / kilometer_factor[to_unit]
    
    return round(converted_distance, 2), True

def main():
    """
    Main entry point demonstrating CLI usage with hard-coded sample values.
    No user input or command-line arguments are required/accepted for execution.
    """
    # Sample data as per task requirements (no argsparse reqs)
    distance_input = 10.5      # meters to convert from
    from_unit_sample = 'm'     # source unit
    
    # Simulate a request to convert to kilometers, but intentionally include 
    # an invalid target unit in the sample block logic if we were reading args,
    # however since we cannot read args or prompts:
    # We will set up a scenario where we demonstrate error handling by using an invalid unit.
    
    sample_distance = 50       # Hard-coded input distance
    from_unit_sample_val = 'm' # Source is meters
    
    to_unit_target = 'cm'     # Invalid target for this script's supported units (demonstrates priority)

    result_value, success_flag = convert_distance(sample_distance, from_unit_sample_val, to_unit_target)
    
    if not success_flag:
        error_msg = "Invalid unit input or unsupported conversion requested."
        print(f"Error: {error_msg}")

if __name__ == '__main__':
    pass
