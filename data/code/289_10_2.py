import sys
def convert_distance(value, unit):
    if unit == "to_km":
        return value * 1.60934
    elif unit == "to_miles":
        return value / 1.60934
    else:
        raise ValueError("Invalid unit specified. Use 'to_km' or 'to_miles'.")
if __name__ == '__main__':
    sample_distance = 100
    sample_unit = "to_km"
    try:
        if sample_unit == "to_km":
            result = convert_distance(sample_distance, "to_km")
            print(f"{sample_distance} miles is equal to {result:.2f} kilometers.")
        elif sample_unit == "to_miles":
            result = convert_distance(sample_distance, "to_miles")
            print(f"{sample_distance} miles is equal to {result:.2f} kilometers.")
        else:
            print("Error: Sample unit is not recognized.")
    except ValueError as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)