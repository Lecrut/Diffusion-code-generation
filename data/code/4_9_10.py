import math

def convert_distance_km_to_miles(km: float) -> float:
    """Convert kilometers to miles using the standard conversion factor."""
    return km * 0.621371

def convert_distance_miles_to_kms(miles: float) -> float:
    """Convert miles to kilometers using the inverse of the standard conversion factor."""
    return miles / 0.621371

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or arguments
    
    # Sample data block
    km_samples = [5, 10, 100]
    
    print("Distance Converter Tool")
    print("=======================")
    
    for value in km_samples:
        miles = convert_distance_km_to_miles(value)
        
        print(f"\nSample Input (Kilometers): {value} km")
        print(f"Converted to Miles:       {miles:.4f} mi")
        
        # Demonstrate reverse conversion using the calculated mile value as input for clarity
        back_kms = convert_distance_miles_to_kms(miles)
        print(f"Verification (Miles -> KMs): {back_kms:.6f} km")