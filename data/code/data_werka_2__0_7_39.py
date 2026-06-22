class LengthConverter:
    M_TO_FT = 3.28084
    FT_TO_M = 1 / M_TO_FT

    def convert(self, value, from_unit, to_unit):
        if (from_unit == 'm' and to_unit == 'ft'):
            return value * self.M_TO_FT
        elif (from_unit == 'ft' and to_unit == 'm'):
            return value * self.FT_TO_M
        else:
            raise ValueError('Unsupported unit conversion')

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'm', 'ft'))
    print(converter.convert(32.8084, 'ft', 'm'))