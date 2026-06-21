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
    meters_value = 10
    feet_value = 32.8084
    converted_feet = converter.convert(meters_value, 'm', 'ft')
    print(f'{meters_value} meters is {converted_feet} feet')
    converted_meters = converter.convert(feet_value, 'ft', 'm')
    print(f'{feet_value} feet is {converted_meters} meters')