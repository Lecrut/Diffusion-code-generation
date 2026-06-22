def adjust_distance(distance, unit):
    if unit == 'miles':
        adjusted_distance = distance * 1.60934
        return f"{adjusted_distance} km"
    elif unit == 'km':
        adjusted_distance = distance / 1.60934
        return f"{adjusted_distance} miles"
    else:
        raise ValueError("Unsupported unit type")

if __name__ == '__main__':
    sample_distance_miles = 5
    sample_distance_km = 8

    print(adjust_distance(sample_distance_miles, 'miles'))
    print(adjust_distance(sample_distance_km, 'km'))