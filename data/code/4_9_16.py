import math

def convert_distance(km: float) -> float:
    """Convert kilometers to miles."""
    return km * 0.621371

def main():
    # Hard-coded sample values as per requirements (no user input, args, or network access)
    
    # Sample conversion from Kilometers to Miles
    km_value = 5.0
    
    print(f"Converting {km_value} kilometers to miles...")
    result_miles = convert_distance(km_value)
    print(f"{km_value} kilometers is equal to {result_miles:.2f} miles.")

if __name__ == '__main__':
    main()