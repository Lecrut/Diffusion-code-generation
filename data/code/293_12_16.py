KILOMETERS_TO_MILES = 0.621371
METERS_TO_FEET = 3.28084

def convert_distance(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == 'kilometers' and to_unit == 'miles':
        return value * KILOMETERS_TO_MILES
    elif from_unit == 'meters' and to_unit == 'feet':
        return value * METERS_TO_FEET
    elif from_unit == 'miles' and to_unit == 'kilometers':
        return value / KILOMETERS_TO_MILES
    elif from_unit == 'feet' and to_unit == 'meters':
        return value / METERS_TO_FEET
    else:
        raise ValueError('Unsupported conversion')
if __name__ == '__main__':
    print(convert_distance(10, 'kilometers', 'miles'))
    print(convert_distance(100, 'meters', 'feet'))
    print(convert_distance(5, 'miles', 'kilometers'))
    print(convert_distance(1000, 'feet', 'meters'))