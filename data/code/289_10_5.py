import sys
def convert_distance(value, unit):
    if unit == "to_km":
        return value * 1.60934
    elif unit == "to_miles":
        return value / 1.60934
    else:
        raise ValueError("Invalid unit specified. Use 'to_km' or 'to_miles'.")
if __name__ == '__main__':
    miles_input = 100
    conversion_type = "to_km"
    try:
        miles = float(miles_input)
        if conversion_type == "to_km":
            result = convert_distance(miles, "to_km")
            print(f"{miles} miles is equal to {result:.2f} kilometers.")
        elif conversion_type == "to_miles":
            result = convert_distance(miles, "to_miles")
            print(f"{miles} miles is equal to {result:.2f} kilometers.")
        else:
            print("Error: Invalid conversion type specified.")
    except ValueError as e:
        print(f"Error: Invalid numerical input or conversion error. Details: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)