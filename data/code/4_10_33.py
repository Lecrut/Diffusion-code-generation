class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_METERS = 1000

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'miles':
            intermediate_value = value * self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS
        elif from_unit == 'kilometers':
            intermediate_value = value * self.KILOMETERS_TO_METERS
        elif from_unit == 'meters':
            intermediate_value = value
        else:
            raise ValueError(f'Unsupported conversion from {from_unit} to meters')
        if to_unit == 'miles':
            return intermediate_value / (self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS)
        elif to_unit == 'kilometers':
            return intermediate_value / self.KILOMETERS_TO_METERS
        elif to_unit == 'meters':
            return intermediate_value
        else:
            raise ValueError(f'Unsupported conversion from meters to {to_unit}')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'meters'))
    print(converter.convert(100, 'meters', 'miles'))