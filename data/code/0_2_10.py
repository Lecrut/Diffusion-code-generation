def convert_kilometers_to_miles(km: float) -> float:
    """Convert kilometers to miles using the standard conversion factor."""
    return km * 0.621371

if __name__ == '__main__':
    # Sample input values as per task requirement (no interactive prompts in this block)
    sample_km = 50.0
    
    try:
        result_miles = convert_kilometers_to_miles(sample_km)
        print(f"{sample_km} kilometers is equal to {result_miles:.2f} miles.")
    except Exception as e:
        # Basic error handling for unexpected issues, though sample input won't trigger it
        print(f"An unexpected error occurred: {e}")