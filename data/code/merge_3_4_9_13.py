"""
Command-Line Tool to Convert Distance between Kilometers and Miles.
This module provides a simple conversion utility with clear prompts 
and includes a sample execution block that runs without user input.
"""

def convert_distance(distance_km: float, distance_miles: float) -> None:
    """
    Display the relationship between kilometers and miles for given values.

    Args:
        distance_km (float): Distance in kilometers to display alongside.
        distance_miles (float): Distance in miles to display alongside.
    """
    print(f"Kilometers ({distance_km:.2f} km) is equivalent to {distance_miles:.2f} miles.")

def get_sample_values() -> tuple[float, float]:
    """
    Returns hard-coded sample values for kilometers and miles 
    that correspond to each other (10 km ≈ 6.2137 mi).
    
    Uses the standard conversion factor: 1 mile = 1.60934 kilometers.
    Sample value chosen: 50 kilometers -> ~31.068 miles.
    """
    sample_km = 50.0
    # Calculate corresponding miles using precise conversion factor
    sample_miles = round(sample_km / 1.60934, 2)
    return sample_km, sample_miles

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input or args needed).
    km_value, miles_value = get_sample_values()
    
    print("--- Distance Converter Sample Output ---")
    convert_distance(km_value, miles_value)

    # Additional demonstration with a different scale for clarity.
    extra_km = 10.0
    extra_miles = round(extra_km / 1.60934, 2)
    
    print("\n--- Another Example ---")
    convert_distance(extra_km, extra_miles)