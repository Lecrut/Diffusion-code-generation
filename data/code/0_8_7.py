def convert_length_to_miles_and_km(length):
    """Converts a given length to miles and kilometers."""
    miles = length / 1609.34
    km = length * 0.000621371
    
    return f"{miles:.2f} miles, {km:.2f} kilometers"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    samples = [50000, 1.84]
    
    for length in samples:
        result = convert_length_to_miles_and_km(length)
        print(result)