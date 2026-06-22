class TimeConverter:
    CONVERSION_FACTORS = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800}

    @staticmethod
    def convert(value, from_unit, to_unit):
        return value * (TimeConverter.CONVERSION_FACTORS[from_unit] / TimeConverter.CONVERSION_FACTORS[to_unit])

if __name__ == '__main__':
    print(TimeConverter.convert(1, 'h', 'm'))
    print(TimeConverter.convert(24, 'd', 's'))
    print(TimeConverter.convert(7, 'w', 'hours'))