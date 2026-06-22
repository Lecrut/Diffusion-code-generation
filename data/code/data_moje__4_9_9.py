def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit.lower() == 'miles' and to_unit.lower() == 'kilometers':
        return value * 1.60934
    if from_unit.lower() == 'kilometers' and to_unit.lower() == 'miles':
        return value / 1.60934
    raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    miles_value = 10
    kilometers_value = convert_distance(miles_value, 'miles', 'kilometers')
    print(kilometers_value)

    kilometers_input = 16.0934
    miles_output = convert_distance(kilometers_input, 'kilometers', 'miles')
    print(miles_output)