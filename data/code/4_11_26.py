def adjust_distance(distance, unit):
    if unit == 'miles':
        return distance * 1.60934, 'km'
    elif unit == 'km':
        return distance / 1.60934, 'miles'
    else:
        raise ValueError("Unsupported unit type")

if __name__ == '__main__':
    sample_distance_miles = 5
    adjusted_distance_km = adjust_distance(sample_distance_miles, 'miles')
    print(f"{sample_distance_miles} miles is {adjusted_distance_km[0]} {adjusted_distance_km[1]}")
    
    sample_distance_km = 8
    adjusted_distance_miles = adjust_distance(sample_distance_km, 'km')
    print(f"{sample_distance_km} km is {adjusted_distance_miles[0]} {adjusted_distance_miles[1]}")