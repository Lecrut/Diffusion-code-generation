def convert_distance(distance, from_unit, to_unit, factor):
    if from_unit == to_unit:
        return distance
    if from_unit == "miles" and to_unit == "kilometers":
        return distance * factor
    elif from_unit == "kilometers" and to_unit == "miles":
        return distance / factor
    else:
        raise ValueError("Unsupported unit conversion.")
if __name__ == '__main__':
    miles = 100
    from_unit = "miles"
    to_unit = "kilometers"
    conversion_factor = 1.60934
    try:
        result = convert_distance(miles, from_unit, to_unit, conversion_factor)
        print(f"Original distance: {miles} {from_unit}")
        print(f"Conversion factor (miles to km): {conversion_factor}")
        print(f"Converted distance: {result:.2f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")