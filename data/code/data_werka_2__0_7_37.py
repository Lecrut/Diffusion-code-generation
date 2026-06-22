class LengthConverter:
    M_TO_F = 3.28084
    F_TO_M = 1 / M_TO_F

    def convert(self, value, from_unit, to_unit):
        if (from_unit, to_unit) == ('m', 'ft'):
            return value * self.M_TO_F
        elif (from_unit, to_unit) == ('ft', 'm'):
            return value * self.F_TO_M
        else:
            raise ValueError('Unsupported unit conversion')

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(20, 'm', 'ft'))
    print(converter.convert(65.6168, 'ft', 'm'))