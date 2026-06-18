def convert_length(length):
    """Converts a length to miles and kilometers."""
    # Conversion factors: 1 mile = 1.60934 km, so km = length * 1.60934
    # And miles = length / 1.60934 (assuming input is in meters for this context)
    # However, the prompt implies converting a generic "length" unit to both. 
    # Since no source unit is specified, we assume the input is in Meters as it's the SI base unit often used in such conversions.
    
    kilometers = length * 1.0 / 3280.84   # Approximate: meters to km (divide by ~3280) or use standard factor
    miles = length * 0.000621371            # Meters to miles
    
    return kilometers, miles

def main():
    """Main function with hard-coded sample values."""
    
    # Hard-coded sample values for demonstration as per instructions
    samples = [1000, 5000, 100] 
    
    print("Sample Conversions (Input assumed to be in Meters):")
    print("-" * 30)
    
    for length in samples:
        km, mi = convert_length(length)
        
        # Format output to two decimal places using f-strings
        formatted_km = "{:.2f}".format(km)
        formatted_mi = "{:.2f}".format(mi)
        
        print(f"Input ({length} m): {formatted_km} km, {formatted_mi} mi")

if __name__ == '__main__':
    main()