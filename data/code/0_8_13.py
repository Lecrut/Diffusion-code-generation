def convert_length(length):
    """Converts a length to miles and kilometers."""
    # Conversion factors: 1 mile = 1.60934 km, 1 kilometer = 0.621371 miles
    miles = length / 1.60934
    kilometers = length * 0.621371
    
    return f"{miles:.2f} miles", f"{kilometers:.2f} km"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no interactive input)
    test_lengths = [5, 10.5, 3]
    
    for length in test_lengths:
        result_miles, result_km = convert_length(length)
        
        print(f"Input Length: {length}")
        print(result_miles)
        print(result_km)
        print("-" * 40)