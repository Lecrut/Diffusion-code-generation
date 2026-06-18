import math

def convert_length_to_miles_and_kilometers(length: float) -> tuple[float, float]:
    """
    Converts a length in feet to miles and kilometers.
    
    Args:
        length (float): The input length value.
        
    Returns:
        tuple: A tuple containing the converted values for miles and kilometers.
               Both values are rounded to two decimal places.
               
    Notes:
        1 mile = 5280 feet
        1 kilometer ≈ 3280.84 feet (or more precisely, 1 km = 1000 meters)
    """
    # Conversion factors relative to feet
    conversion_to_miles_factor = length / 5280
    conversion_to_kilometers_factor = (length * 0.3048)

    return round(conversion_to_miles_factor, 2), round(conversion_to_kilometers_factor, 2)

if __name__ == '__main__':
    pass
