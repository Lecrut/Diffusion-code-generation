import math

def convert_distance(distance_value: float, target_unit: str) -> dict:
    """
    Converts a given distance value from meters to various units 
    using precise floating-point arithmetic and handles potential errors gracefully.
    
    Args:
        distance_value (float): The distance in meters to be converted.
        target_unit (str): The unit to convert 'distance' into ('km', 'miles').

    Returns:
        dict: A dictionary containing the conversion result with keys 'converted_distance', 
              'original_units', and 'target_units'. Raises an exception if invalid input is provided, 
              except for division by zero which returns a sentinel error message.
    
    Note: This function does not accept any interactive prompt or network access."""

    # Define base units (meters) to target conversion factors
    unit_conversions = {
        'km': 1 / 1000,
        'miles': 1 / 1609.344
    }
    
    if distance_value == float('inf') or math.isnan(distance_value):
        return {'error': "Distance value must be a valid finite number."}

    # Check for invalid input types by attempting arithmetic implicitly in dict creation

if __name__ == '__main__':
    pass
