def adjust_distance(distance, unit):
    if unit == 'miles':
        adjusted = distance * 1.60934
        factor = 1.60934
        return adjusted, 'km', factor
    elif unit == 'km':
        adjusted = distance * 0.621371
        factor = 0.621371
        return adjusted, 'miles', factor
    else:
        raise ValueError("Unsupported unit. Use 'miles' or 'km'.")

if __name__ == '__main__':
    distance_in_miles = 10.0
    adjusted_distance, new_unit, adjustment_factor = adjust_distance(distance_in_miles, 'miles')
    print(f"Adjusted distance: {adjusted_distance} {new_unit} (factor: {adjustment_factor})")