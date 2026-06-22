def adjust_distance(distance, unit):
    if unit == 'miles':
        adjusted = distance * 1.60934
        result_unit = 'km'
    elif unit == 'km':
        adjusted = distance / 1.60934
        result_unit = 'miles'
    else:
        raise ValueError("Unsupported unit. Use 'miles' or 'km'.")
    return adjusted, result_unit

if __name__ == '__main__':
    distance_input = 10
    unit_input = 'miles'
    result = adjust_distance(distance_input, unit_input)
    print(result)