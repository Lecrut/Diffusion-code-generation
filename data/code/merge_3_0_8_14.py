def convert_length(length_miles):
    """Converts a length given in miles to both kilometers and meters."""
    km = length_miles * 1.60934
    return round(km, 2)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    samples = [5.0, 10.5, 25]

    for miles in samples:
        kilometers = convert_length(miles)
        
        print(f"Input (miles): {miles}")
        print(f"Miles to Kilometers: {kilometers:.2f} km")