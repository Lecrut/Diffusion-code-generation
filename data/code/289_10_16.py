def validate_km(km):
    if not isinstance(km, (int, float)) or km < 0:
        raise ValueError("Invalid input for kilometers. Must be a non-negative number.")

def convert_to_miles(km):
    return round(km * 0.621371, 2)

if __name__ == '__main__':
    sample_km = 100
    try:
        validate_km(sample_km)
        miles = convert_to_miles(sample_km)
        print(f"{sample_km} kilometers is equal to {miles:.2f} miles.")
    except ValueError as e:
        print(f"Error: Invalid input provided. Details: {e}")