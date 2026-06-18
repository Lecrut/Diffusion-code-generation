import sys

def kilometers_to_miles(km: float) -> float:
    """Convert distance in kilometers to miles."""
    return km * 0.621371

def convert_distance() -> None:
    """Perform a sample conversion from kilometers to miles using hard-coded values."""
    
    # Hardcoded sample value for demonstration (as per task requirement)
    # This runs without user input, command-line arguments, network access, or pre-existing files.
    distance_km = 100.5
    
    print(f"Converting {distance_km} kilometers to miles...")
    result_miles = kilometers_to_miles(distance_km)
    
    formatted_result = f"{result_miles:.2f}"
    print(f"The equivalent is {formatted_result} miles.")

if __name__ == '__main__':
    convert_distance()