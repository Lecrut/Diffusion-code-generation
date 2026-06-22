def convert_distance(distance, target_unit):
    units = {
        'km': 1.0,
        'm': 1000.0,
        'cm': 100000.0,
        'mm': 1000000.0,
        'mi': 0.621371,
        'yd': 1093.61,
        'ft': 3280.84,
        'in': 39370.1
    }

    if target_unit not in units:
        raise ValueError("Unsupported target unit")

    try:
        conversion_factor = units[target_unit]
        return distance * conversion_factor
    except ZeroDivisionError:
        return None

if __name__ == '__main__':
    result1 = convert_distance(1, 'km')
    print(result1)
    result2 = convert_distance(1, 'mi')
    print(result2)
    result3 = convert_distance(1000, 'm')
    print(result3)
    result4 = convert_distance(5280, 'ft')
    print(result4)
    result5 = convert_distance(1, 'in')
    print(result5)
    result6 = convert_distance(1, 'yd')
    print(result6)
    result7 = convert_distance(1, 'cm')
    print(result7)
    result8 = convert_distance(1, 'mm')
    print(result8)
    try:
        result9 = convert_distance(1, 'ly')
        print(result9)
    except ValueError:
        print("Unsupported unit handled")