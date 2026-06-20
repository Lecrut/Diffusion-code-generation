def convert_distance(value, from_unit, to_unit, factor):
    if from_unit == to_unit:
        return value
    if from_unit == 'miles' and to_unit == 'kilometers':
        return value * factor
    if from_unit == 'kilometers' and to_unit == 'miles':
        return value / factor
    raise ValueError('Invalid unit combination')

if __name__ == '__main__':
    miles_value = 60
    kilometers_value = 100
    conversion_factor = 1.60934
    converted_miles = convert_distance(miles_value, 'miles', 'kilometers', conversion_factor)
    converted_kilometers = convert_distance(kilometers_value, 'kilometers', 'miles', conversion_factor)
    print(converted_miles)
    print(converted_kilometers)