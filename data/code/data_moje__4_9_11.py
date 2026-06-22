MILES_TO_KILOMETERS = 1.60934

def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit.lower() == 'miles' and to_unit.lower() == 'kilometers':
        return value * MILES_TO_KILOMETERS
    if from_unit.lower() == 'kilometers' and to_unit.lower() == 'miles':
        return value / MILES_TO_KILOMETERS
    raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")

if __name__ == '__main__':
    sample_miles = 10.0
    sample_km = 5.0
    print(convert_distance(sample_miles, 'miles', 'kilometers'))
    print(convert_distance(sample_km, 'kilometers', 'miles'))