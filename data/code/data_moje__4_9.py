def convert_distance(value, source_unit, target_unit, conversion_factor):
    if source_unit == target_unit:
        return value
    if source_unit == "miles" and target_unit == "kilometers":
        return value * conversion_factor
    if source_unit == "kilometers" and target_unit == "miles":
        return value / conversion_factor
    raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    miles_to_km_factor = 1.60934
    distance_miles = 5
    distance_km = convert_distance(distance_miles, "miles", "kilometers", miles_to_km_factor)
    print(f"{distance_miles} miles is {distance_km} kilometers")
    back_to_miles = convert_distance(distance_km, "kilometers", "miles", miles_to_km_factor)
    print(f"{distance_km} kilometers is {back_to_miles} miles")