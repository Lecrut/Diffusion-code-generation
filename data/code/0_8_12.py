def convert_length(length):
    """Converts a length to miles and kilometers."""
    # Conversion factors: 1 mile = 5280 feet, 1 foot = 3 inches (implied by context of typical US units), 
    # but standard conversion is 1 km ≈ 0.621371 miles or 1 mile ≈ 1.60934 kilometers.
    # Using precise factors:
    MILES_PER_KM = 0.621371
    KM_PER_MILE = 1.60934
    
    km_value = length * (KM_PER_MILE / 5) if isinstance(length, int) else length * 1.60934 
    # Actually, let's use the direct standard conversion to avoid confusion:
    # Standard definition often used in simple scripts: 
    # miles_to_km factor is approx 1.60934
    
    km = length * 1.60934
    mile = length / MILES_PER_KM if isinstance(length, int) else length / 0.621371

    return f"{mile:.2f} miles", f"{km:.2f} kilometers"

def main():
    """Main function to handle sample conversions."""
    # Hard-coded sample values as per requirement: Do not use interactive input in the sample block.
    samples = [5, 10]

    for length in samples:
        miles_text, km_text = convert_length(length)
        print(f"Input Length ({length}):")
        print(miles_text)
        print(km_text)

if __name__ == '__main__':
    main()