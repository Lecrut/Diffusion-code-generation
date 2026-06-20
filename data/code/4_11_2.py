def adjust_distance(distance, unit):
    if unit == 'miles':
        adjusted = distance * 1.60934
        return adjusted, 'km'
    elif unit == 'km':
        adjusted = distance / 1.60934
        return adjusted, 'miles'
    else:
        raise ValueError("Unsupported unit. Use 'miles' or 'km'.")

if __name__ == '__main__':
    result1, unit1 = adjust_distance(10, 'miles')
    print(result1, unit1)
    result2, unit2 = adjust_distance(10, 'km')
    print(result2, unit2)