def adjust_distance(distance, unit):
    if unit == 'miles':
        return distance * 1.60934, 'km'
    elif unit == 'km':
        return distance / 1.60934, 'miles'
    else:
        raise ValueError("Unsupported unit type")

if __name__ == '__main__':
    sample_distance_miles = 5
    adjusted_distance_km, new_unit_km = adjust_distance(sample_distance_miles, 'miles')
    print(f"{sample_distance_miles} miles is {adjusted_distance_km:.2f} {new_unit_km}")

    sample_distance_km = 10
    adjusted_distance_miles, new_unit_miles = adjust_distance(sample_distance_km, 'km')
    print(f"{sample_distance_km} km is {adjusted_distance_miles:.2f} {new_unit_miles}")