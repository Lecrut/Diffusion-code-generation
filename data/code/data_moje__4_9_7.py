def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'miles' and to_unit == 'kilometers':
        return value * 1.60934
    if from_unit == 'kilometers' and to_unit == 'miles':
        return value / 1.60934
    raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    sample_miles = 10.0
    sample_kilometers = convert_distance(sample_miles, 'miles', 'kilometers')
    print(sample_kilometers)
    sample_km = 5.0
    sample_mi = convert_distance(sample_km, 'kilometers', 'miles')
    print(sample_mi)