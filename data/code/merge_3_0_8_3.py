import sys

def convert_length(length_miles):
    """Converts miles to kilometers."""
    km = length_miles * 1.60934
    return round(km, 2)

if __name__ == '__main__':
    # Sample values hard-coded as per task requirements
    sample_lengths = [1.5, 5.0]
    
    for miles in sample_lengths:
        km_value = convert_length(miles)
        
        print(f"Miles input: {miles}")
        print("Converted Values:")
        print(f"   Kilometers: {km_value:.2f} mi")
        sys.exit(0)