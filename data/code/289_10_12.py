def validate_km(km):
    if not isinstance(km, (int, float)):
        raise ValueError("Input must be a number.")

def convert_km_to_miles(km):
    validate_km(km)
    return km * 0.621371

if __name__ == '__main__':
    sample_km = 100
    try:
        miles_result = convert_km_to_miles(sample_km)
        print(f"{sample_km} kilometers is equal to {miles_result:.2f} miles.")
    except ValueError as e:
        print(f"Error: Invalid input provided. Details: {e}", file=sys.stderr)