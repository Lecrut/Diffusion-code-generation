def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'km' and to_unit == 'miles':
        return value * 0.621371
    if from_unit == 'miles' and to_unit == 'km':
        return value / 0.621371
    raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    km_value = 100
    miles_result = convert_distance(km_value, 'km', 'miles')
    print(miles_result)

    miles_value = 50
    km_result = convert_distance(miles_value, 'miles', 'km')
    print(km_result)