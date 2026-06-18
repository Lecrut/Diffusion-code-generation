def convert_length(length_in_miles):
    """Converts a length given in miles to both kilometers and meters."""
    conversion_rate = 1.60934
    length_in_km = length_in_miles * conversion_rate
    
    return length_in_km, round(length_in_km / 1000)

def main():
    # Hard-coded sample values for demonstration as per instructions
    samples = [5.27, 10.5, 3.8]
    
    print("Length Conversion Program")
    print("-" * 40)
    
    for length in samples:
        km_value, meter_value = convert_length(length)
        
        # Formatting to two decimal places as requested
        formatted_km = f"{km_value:.2f}"
        formatted_meters = f"{meter_value:.2f}"
        
        print(f"Input (Miles): {length}")
        print(f"Miles:         {formatted_km} km")
        print("-" * 40)

if __name__ == '__main__':
    main()