class LengthConverter:

    def __init__(self):
        self.conversion_factors = {'m_to_ft': 3.28084, 'ft_to_m': 1 / 3.28084}

    def convert(self, value, from_unit, to_unit):
        if from_unit == 'm' and to_unit == 'ft':
            return value * self.conversion_factors['m_to_ft']
        elif from_unit == 'ft' and to_unit == 'm':
            return value * self.conversion_factors['ft_to_m']
        else:
            raise ValueError('Unsupported unit conversion')
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(5, 'm', 'ft'))
    print(converter.convert(16.4042, 'ft', 'm'))