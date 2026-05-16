def convert_distance(value, from_unit, to_unit, factor):
    if from_unit == to_unit:
        return value
    if from_unit == "miles" and to_unit == "kilometers":
        return value * factor
    elif from_unit == "kilometers" and to_unit == "miles":
        return value / factor
    else:
        raise ValueError("Unsupported unit conversion requested.")
if __name__ == '__main__':
    distance_miles = 100.0
    from_unit = "miles"
    to_unit = "kilometers"
    conversion_factor = 1.60934
    try:
        result = convert_distance(distance_miles, from_unit, to_unit, conversion_factor)
        print(f"Original distance in {from_unit}: {distance_miles}")
        print(f"Conversion factor (miles to km): {conversion_factor}")
        print(f"Converted distance in {to_unit}: {result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")