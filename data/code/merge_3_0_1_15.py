import math

def convert_length(length: float, unit: str) -> float:
    """
    Converts a given length from its source unit to meters.
    
    Supported units (case-insensitive): 'm' (meters), 'ft' (feet), 
    'cm' (centimeters), 'in' (inches).
    
    Parameters:
        length (float): The numerical value of the length.
        unit (str): The string representation of the source unit ('m', 'ft', 'cm', or 'in').
        
    Returns:
        float: The converted length in meters.
        
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    
    # Conversion factors to meters
    conversion_factors = {
        'm': 1,
        'ft': 0.3048,
        'cm': 0.01,
        'in': 0.0254
    }

    if unit.lower() not in conversion_factors:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are m, ft, cm, and in.")

    return length * conversion_factors[unit.lower()]

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print("10 meters:", convert_length(10, 'm'))  # Expected: 10.0
    
    print("5 feet:", convert_length(5, 'ft'))      # Expected: ~1.524
    
    print("2 centimeters:", convert_length(2, 'cm'))  # Expected: 0.02
    
    print("36 inches:", convert_length(36, 'in'))   # Expected: 0.9144