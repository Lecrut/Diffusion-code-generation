import sys
def convert_distance(distance, from_unit, to_unit, factor):
    if from_unit == to_unit:
        return distance
    if from_unit == "miles" and to_unit == "kilometers":
        return distance * factor
    elif from_unit == "kilometers" and to_unit == "miles":
        return distance / factor
    else:
        raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    distance_value = 100
    from_unit = "miles"
    to_unit = "kilometers"
    conversion_factor = 1.60934
    try:
        result = convert_distance(distance_value, from_unit, to_unit, conversion_factor)
        print(f"Original Distance: {distance_value} {from_unit}")
        print(f"Conversion Factor (1 {from_unit} = {conversion_factor} km): {conversion_factor}")
        print(f"Converted Distance: {result:.2f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)