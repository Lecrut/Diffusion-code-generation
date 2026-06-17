def convert_distance(distance, unit):
    if unit == 'miles':
        return distance
    elif unit == 'km':
        return distance * 1.60934
    else:
        raise ValueError("Invalid unit type. Must be 'miles' or 'km'.")
if __name__ == '__main__':
    distance_miles = 10.0
    unit_miles = 'miles'
    converted_miles = convert_distance(distance_miles, unit_miles)
    print(f"Converted {distance_miles} {unit_miles} to km: {convert_distance(distance_miles, 'km')}")
    distance_km = 10.0
    unit_km = 'km'
    converted_km = convert_distance(distance_km, unit_km)
    print(f"Converted {distance_km} {unit_km} to miles: {convert_distance(distance_km, 'miles')}")
    distance_miles_2 = 5.5
    unit_miles_2 = 'miles'
    converted_miles_2 = convert_distance(distance_miles_2, unit_miles_2)
    print(f"Converted {distance_miles_2} {unit_miles_2} to km: {convert_distance(distance_miles_2, 'km')}")