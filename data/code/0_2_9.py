import sys

def km_to_miles(km_value, miles_per_km):
    """Convert kilometers to miles using a custom conversion factor."""
    return float(km_value) * miles_per_km

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no interactive input)
    input_kilometers = 50.75
    miles_per_km_factor = 26 / 18
    
    try:
        result_miles = km_to_miles(input_kilometers, miles_per_km_factor)
        print(f"{input_kilometers} kilometers is approximately {result_miles:.4f} miles.")
    except Exception as e:
        print(f"An error occurred during calculation: {e}")