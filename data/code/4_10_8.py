def convert_distance(value, from_unit, to_unit, factor):
    if from_unit == to_unit:
        return value
    if from_unit == "miles" and to_unit == "kilometers":
        return value * factor
    elif from_unit == "kilometers" and to_unit == "miles":
        return value / factor
    else:
        raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    miles = 100
    conversion_factor = 1.60934
    target_unit = "kilometers"
    try:
        result = convert_distance(miles, "miles", target_unit, conversion_factor)
        print(f"Original distance in miles: {miles}")
        print(f"Conversion factor (miles to km): {conversion_factor}")
        print(f"Converted distance in kilometers: {result}")
    except ValueError as e:
        print(f"Error: {e}")