def adjust_distance(distance, unit1, unit2):
    if unit1 == unit2:
        return distance, 1.0
    elif unit1 == 'miles' and unit2 == 'km':
        conversion_factor = 1.60934
        result = distance * conversion_factor
        return result, conversion_factor
    elif unit1 == 'km' and unit2 == 'miles':
        conversion_factor = 0.621371
        result = distance * conversion_factor
        return result, conversion_factor
    else:
        raise ValueError("Unsupported unit combination")
if __name__ == '__main__':
    distance_value = 10
    unit_a = 'miles'
    unit_b = 'km'
    try:
        result, factor = adjust_distance(distance_value, unit_a, unit_b)
        print(f"Original distance: {distance_value} {unit_a}")
        print(f"Adjusted distance: {result} {unit_b}")
        print(f"Adjustment factor: {factor}")
    except ValueError as e:
        print(f"Error: {e}")