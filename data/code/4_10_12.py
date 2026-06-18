import math

def convert_distance_miles_to_kilometers(miles: float) -> float:
    """Convert a distance in miles to kilometers using standard conversion factor."""
    return miles * 1.60934

def convert_distance_km_to_miles(kilometers: float) -> float:
    """Convert a distance in kilometers back to miles using the inverse of the conversion factor."""
    return kilometers / 1.60934

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies
    
    # Sample data
    miles_sample = 5.0
    km_sample = 25.0
    
    print(f"Conversion Demonstration")
    print("-" * 30)
    
    result1 = convert_distance_miles_to_kilometers(miles_sample)
    print(f"Miles ({miles_sample}) to Kilometers: {result1:.4f}")
    
    # Verify reverse conversion accuracy within floating-point tolerance
    verified_km = round(result1, 2)
    miles_back = convert_distance_km_to_miles(verified_km)
    is_accurate = abs(miles_back - miles_sample) < 0.0001
    
    print(f"Verification: {result1:.4f} km converted back to {miles_back:.4f} mi (Accurate: {is_accurate})")