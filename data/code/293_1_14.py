class DistanceConverter:
    KILOMETERS_TO_MILES = 0.621371
    MILES_TO_KILOMETERS = 1 / KILOMETERS_TO_MILES

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == 'km' and to_unit == 'mi':
            return value * DistanceConverter.KILOMETERS_TO_MILES
        elif from_unit == 'mi' and to_unit == 'km':
            return value * DistanceConverter.MILES_TO_KILOMETERS
        elif from_unit == to_unit:
            return value
        else:
            raise ValueError(f'Unsupported conversion: {from_unit} to {to_unit}')
if __name__ == '__main__':
    print(DistanceConverter.convert(10, 'km', 'mi'))
    print(DistanceConverter.convert(5, 'mi', 'km'))
    print(DistanceConverter.convert(15, 'km', 'km'))