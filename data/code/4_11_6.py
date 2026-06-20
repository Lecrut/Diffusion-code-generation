def adjust_distance(distance, unit):
    if unit == 'miles':
        converted = distance * 1.60934
        result_unit = 'km'
    elif unit == 'km':
        converted = distance / 1.60934
        result_unit = 'miles'
    else:
        raise ValueError("Unsupported unit. Use 'miles' or 'km'.")
    
    return converted, result_unit

if __name__ == '__main__':
    value, unit = adjust_distance(10, 'miles')
    print(value, unit)