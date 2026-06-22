class TimeConverter:
    def __init__(self):
        self.conversion_factors = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400,
            'weeks': 604800
        }

    def convert(self, value, from_unit, to_unit):
        return value * (self.conversion_factors[from_unit] / self.conversion_factors[to_unit])

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert(1, 'hours', 'minutes'))
    print(converter.convert(24, 'days', 'seconds'))
    print(converter.convert(7, 'weeks', 'hours'))