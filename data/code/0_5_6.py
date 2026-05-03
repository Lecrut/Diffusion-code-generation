def convert_length(length_str, target_unit):
    conversion_map = {
        'm': 3.28084,
        'ft': 0.3048,
        'in': 0.0254,
        'km': 1000.0,
        'mi': 1609.34,
    }
    if target_unit not in conversion_map:
        return "Error: Invalid target unit"
    try:
        length = float(length_str)
        if target_unit == 'm':
            return length
        elif target_unit == 'ft':
            return length / 0.3048
        elif target_unit == 'in':
            return length / 0.0254
        elif target_unit == 'km':
            return length / 1000.0
        elif target_unit == 'mi':
            return length / 1609.34
        else:
            return "Error: Conversion logic missing for this unit"
    except ValueError:
        return "Error: Invalid length input"
if __name__ == '__main__':
    print(convert_length("10", "ft"))
    print(convert_length("5", "m"))
    print(convert_length("100", "in"))
    print(convert_length("1", "km"))
    print(convert_length("10", "unknown"))
    print(convert_length("abc", "ft"))