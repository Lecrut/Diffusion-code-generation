def adjust_distance(distance, unit):
    if unit == 'miles':
        factor = 1.60934
        result = distance * factor
        return result, 'km', factor
    elif unit == 'km':
        factor = 0.621371
        result = distance * factor
        return result, 'miles', factor
    else:
        raise ValueError("Unit must be 'miles' or 'km'")

if __name__ == '__main__':
    result, new_unit, factor = adjust_distance(10, 'miles')
    print(result, new_unit, factor)
    result, new_unit, factor = adjust_distance(10, 'km')
    print(result, new_unit, factor)