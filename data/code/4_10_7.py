def convert_distance(distance, unit_from, unit_to, conversion_factor):
    if unit_from == unit_to:
        return distance
    if unit_from == "miles" and unit_to == "kilometers":
        return distance * conversion_factor
    elif unit_from == "kilometers" and unit_to == "miles":
        return distance / conversion_factor
    else:
        raise ValueError("Unsupported unit conversion requested.")
if __name__ == '__main__':
    distance_value = 100
    unit_from = "miles"
    unit_to = "kilometers"
    conversion_factor = 1.60934
    try:
        result = convert_distance(distance_value, unit_from, unit_to, conversion_factor)
        print(f"Original Distance: {distance_value} {unit_from}")
        print(f"Conversion Factor (miles to km): {conversion_factor}")
        print(f"Converted Distance: {result:.2f} {unit_to}")
    except ValueError as e:
        print(f"Error: {e}")