def adjust_distance(distance, unit):
    if unit == 'miles':
        adjusted_distance = distance * 1.60934
        return f"{adjusted_distance} km"
    elif unit == 'km':
        adjusted_distance = distance / 1.60934
        return f"{adjusted_distance} miles"
    else:
        return "Invalid unit"

if __name__ == '__main__':
    sample_distance_miles = 5
    sample_unit_miles = 'miles'
    print(adjust_distance(sample_distance_miles, sample_unit_miles))
    
    sample_distance_km = 10
    sample_unit_km = 'km'
    print(adjust_distance(sample_distance_km, sample_unit_km))