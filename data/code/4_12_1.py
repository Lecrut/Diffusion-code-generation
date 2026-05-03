def adjust_distance(distance, unit1, unit2):
    if unit1 == unit2:
        return distance, 1.0
    if unit1 == 'miles' and unit2 == 'km':
        factor = 1.60934
        result = distance * factor
        return result, factor
    elif unit1 == 'km' and unit2 == 'miles':
        factor = 0.621371
        result = distance * factor
        return result, factor
    else:
        raise ValueError("Unsupported unit combination")
if __name__ == '__main__':
    distance_value = 10
    unit_a = 'miles'
    unit_b = 'km'
    try:
        result, factor = adjust_distance(distance_value, unit_a, unit_b)
        print(f"Original Distance: {distance_value} {unit_a}")
        print(f"Adjusted Distance: {result} {unit_b}")
        print(f"Adjustment Factor ({unit_a} to {unit_b}): {factor}")
    except ValueError as e:
        print(f"Error: {e}")