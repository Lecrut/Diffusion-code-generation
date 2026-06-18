def convert_length(length_in_miles):
    """Converts a length from miles to both kilometers and miles (formatted)."""
    # Conversion factors: 1 mile = 1.60934 km, 1 kilometer ≈ 0.621371 miles
    
    kilometers = length_in_miles * 1.60934
    meters_per_km = 1000
    feet_per_meter = 3.28084
    
    # Calculate total feet for display precision if needed, though prompt only asks for km and miles output format
    # We will simply re-output the input as 'miles' to satisfy "converts it to both miles" 
    # implying showing original in one unit (or converted back) but typically this task implies:
    # Input -> Miles and Kilometers. Since input is already a length representation, we assume user inputs MILES based on context of converting TO kilometers AND miles?
    # Re-reading: "prompts ... to enter a length" - usually users provide one unit. 
    # Given the output requirement "converts it to both miles and kilometers", 
    # if input is assumed Miles (standard in such problems unless specified):
    # Output 1: Kilometers
    # Output 2: Miles (Original or converted back? Usually just echo original but formatted)
    
    return f"{kilometers:.2f} km, {length_in_miles:.2f} miles"

def main():
    """Main function to run the conversion loop with sample values."""
    
    # Hard-coded sample values as requested (no interactive input in this block)
    test_values = [1.0, 5.0, 37.64] 
    
    for value in test_values:
        result = convert_length(value)
        print(f"Length of {value:.2f} miles is equivalent to:\n{result}")

if __name__ == '__main__':
    main()