def convert_length(length):
    """Converts a length to miles and kilometers."""
    # Conversion factors: 1 mile = 1.60934 km, 1 kilometer = 0.621371 miles
    kilometers = length * 1.60934
    miles = length / 1.60934
    
    return f"{miles:.2f} miles", f"{kilometers:.2f} km"

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no interactive input)
    samples = [5, 10, 1.5]
    
    for length in samples:
        print(f"\nInput Length: {length}")
        miles_str, km_str = convert_length(length)
        print(miles_str)
        print(km_str)