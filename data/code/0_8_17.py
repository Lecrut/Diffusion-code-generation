def convert_length(length):
    """Converts a length to miles and kilometers."""
    miles = length / 1609.34
    kilometers = length * 0.000621371
    
    return f"{miles:.2f} miles", f"{kilometers:.2f} km"

if __name__ == '__main__':
    # Hard-coded sample values as per instructions to avoid interactive input in the main block
    sample_inputs = [50, 1609.34, 1]
    
    print("Converting lengths:")
    for length in sample_inputs:
        miles_str, km_str = convert_length(length)
        print(f"Length ({length}): {miles_str}, {km_str}")