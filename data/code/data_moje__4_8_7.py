import math

def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if (from_unit == 'km' and to_unit == 'miles') or (from_unit == 'kilometers' and to_unit == 'miles'):
        return value / 1.609344
    if (from_unit == 'miles' and to_unit == 'km') or (from_unit == 'miles' and to_unit == 'kilometers'):
        return value * 1.609344
    raise ValueError("Unsupported unit conversion")

def format_result(value, unit):
    return round(value, 4)

if __name__ == '__main__':
    test_value = 10
    test_from = 'km'
    test_to = 'miles'
    result = convert_distance(test_value, test_from, test_to)
    formatted_result = format_result(result, test_to)
    print(formatted_result)
    
    test_value_2 = 50
    test_from_2 = 'miles'
    test_to_2 = 'kilometers'
    result_2 = convert_distance(test_value_2, test_from_2, test_to_2)
    formatted_result_2 = format_result(result_2, test_to_2)
    print(formatted_result_2)