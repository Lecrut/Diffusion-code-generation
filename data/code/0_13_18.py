import math

def convert_to_meters(length_km):
    """Convert length from kilometers to meters."""
    return length_km * 1000

def convert_to_feet(meters):
    """Convert length from meters to feet using the standard conversion factor (1 meter = 3.28084 feet)."""
    return meters * 3.28084

if __name__ == '__main__':
    # Hard-coded sample values in kilometers for demonstration purposes
    measurements_in_km = [5, 10, 7.5]

    print("Length Conversions from Kilometers")
    print("-" * 30)

    try:
        for km_value in measurements_in_km:
            meters_val = convert_to_meters(km_value)
            feet_val = convert_to_feet(meters_val)
            
            # Format output with appropriate precision (2 decimal places)
            formatted_output = f"{km_value} km" \
                               + "=" \
                               + f"{meters_val:.1f}" \
                               + " m\n" \
                               + "\t\t= " \
                               + f"{feet_val:.4f}\n"

            print(formatted_output)
    except TypeError as e:
        # Handle cases where input might not be a number if extended to accept lists of mixed types later
        print(f"Error processing measurements: {e}")