def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'km' and to_unit == 'miles':
        return value * 0.621371
    if from_unit == 'miles' and to_unit == 'km':
        return value / 0.621371
    raise ValueError("Unsupported units or direction")

def format_result(value, to_unit):
    return f"{value:.2f} {to_unit}"

if __name__ == '__main__':
    km_to_miles = convert_distance(100, 'km', 'miles')
    miles_to_km = convert_distance(50, 'miles', 'km')
    print(format_result(km_to_miles, 'miles'))
    print(format_result(miles_to_km, 'km'))