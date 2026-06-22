def adjust_distance(distance, unit):
    if unit == 'miles':
        factor = 1.60934
        converted_value = distance * factor
        return converted_value, factor, 'km'
    elif unit == 'km':
        factor = 0.621371
        converted_value = distance / factor
        return converted_value, factor, 'miles'
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    distance_val = 10
    unit_val = 'miles'
    result, adj_factor, target_unit = adjust_distance(distance_val, unit_val)
    print(f"Adjusted distance: {result} {target_unit} (factor: {adj_factor})")