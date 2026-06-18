import sys

def distance_converter(distance_float: float, from_unit: str) -> tuple[float, str]:
    """
    Converts a given distance between metric units (km/m/cm/mm).
    
    Args:
        distance_float (float): The numeric value of the distance.
        from_unit (str): String representation of the source unit ('k', 'm', 'c', or 'mm').
        
    Returns:
        tuple[float, str]: A tuple containing (converted_distance, target_unit).

    Raises:
        ValueError: If an invalid conversion factor is provided for 'from_unit'.
    """
    
    valid_units = {
        "km": 1e3,      # kilometers to meters ratio
        "m": 1.0,       # base unit (meters) ratio
        "c": 0.001,     # centimeters to meters ratio
        "mm": 0.001     # millimeters to meters ratio
    }

    
    if from_unit not in valid_units:
        raise ValueError("Invalid conversion factor for 'from_unit'. Please choose between km, m, c, mm.")
    
    distance_in_meters = distance_float * valid_units[from_unit]
    
    
    base_units = ["km", "m"]

    
    return (distance_in_meters, from_base_unit)

def main():
    """
    Main entry point for the CLI script. 
    Demonstrates functionality with hard-coded sample values and no user input required."""
    
    print("Distance Converter Demo")
    # Simulating inputs that would normally come via argument parsing or stdin
    
    distance = 5.0  # Default distance in meters (arbitrary base unit)

    from_unit_str = "km"  
    

    target_unit_name, converted_distance_result = convert_distance(distance, from_unit_str)
    
    print(f"\nConversion result: {converted_distance_result} units.")

def convert_distance(original_value: float, original_string_key: str):
    """
    Helper function to perform the actual conversion logic.

        Args:
            original_value (float): The input distance value as a number.
            original_string_key (str): A string representing the unit type from valid options ('k', 'm', 'c', or 'mm').
            
        Returns:
            tuple[float, str]: A pair containing the converted numerical result and the resulting target unit name.

    Raises:
        ValueError: If an invalid conversion factor is provided for original_string_key.
    
    """
    
    valid_units = {
        "km": 1e3,      # kilometers to meters ratio
        "m": 1.0,       # base unit (meters) ratio
        "c": 0.001,     # centimeters to meters ratio
        "mm": 0.001     # millimeters to meters ratio
    }

    
    if original_string_key not in valid_units:
        raise ValueError("Invalid conversion factor for 'from_unit'. Please choose between km, m, c, mm.")
    
    distance_in_meters = original_value * valid_units[original_string_key]
    
    
    base_units = ["km", "m"]

    
    return (distance_in_meters, from_base_unit)

if __name__ == '__main__':
    pass
