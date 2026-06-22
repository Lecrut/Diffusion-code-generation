class TimeConverter:
    def __init__(self):
        self.conversion_factors = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800}

    def convert(self, value, from_unit, to_unit):
        return value * (self.conversion_factors[from_unit] / self.conversion_factors[to_unit])

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert(1, 'h', 'm'))
    print(converter.convert(24, 'd', 's'))
    print(converter.convert(7, 'w', 'hours'))