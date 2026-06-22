def convert_distance(distance, from_unit, to_unit):
    if from_unit == to_unit:
        return distance
    if from_unit == 'km' and to_unit == 'mi':
        return distance * 0.621371
    if from_unit == 'mi' and to_unit == 'km':
        return distance * 1.60934
    raise ValueError("Unsupported unit conversion")

def format_conversion_result(distance, from_unit, to_unit):
    result = convert_distance(distance, from_unit, to_unit)
    return f"{distance} {from_unit} = {result:.4f} {to_unit}"

if __name__ == '__main__':
    print(format_conversion_result(10, 'km', 'mi'))
    print(format_conversion_result(5, 'mi', 'km'))
    print(format_conversion_result(100, 'km', 'mi'))
    print(format_conversion_result(25, 'mi', 'km'))