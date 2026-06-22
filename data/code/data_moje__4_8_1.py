def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit.lower() == 'km' and to_unit.lower() == 'miles':
        return value * 0.621371
    if from_unit.lower() == 'miles' and to_unit.lower() == 'km':
        return value / 0.621371
    raise ValueError("Unsupported units. Use 'km' or 'miles'.")

if __name__ == '__main__':
    print(convert_distance(100, 'km', 'miles'))
    print(convert_distance(50, 'miles', 'km'))