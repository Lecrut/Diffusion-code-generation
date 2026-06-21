class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_METERS = 1000

    def __init__(self):
        self.unit_map = {
            'miles': {'kilometers': self.MILES_TO_KILOMETERS, 'meters': self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS},
            'kilometers': {'miles': 1 / self.MILES_TO_KILOMETERS, 'meters': self.KILOMETERS_TO_METERS},
            'meters': {'miles': 1 / (self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS), 'kilometers': 1 / self.KILOMETERS_TO_METERS}
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.unit_map or to_unit not in self.unit_map[from_unit]:
            raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')
        return value * self.unit_map[from_unit][to_unit]

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'meters'))
    print(converter.convert(100, 'meters', 'miles'))