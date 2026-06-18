def convert_kilometers_to_miles(km: float) -> float:
    """Convert a distance in kilometers to miles."""
    return km * 0.621371

if __name__ == '__main__':
    # Sample inputs as per task requirement (no interactive input here)
    sample_kilometers = 50.0
    
    result_miles = convert_kilometers_to_miles(sample_kilometers)
    
    print(f"{sample_kilometers} kilometers is equal to {result_miles:.2f} miles.")