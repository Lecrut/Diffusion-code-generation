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
    sample_length_meters = 25.0
    sample_length_feet = 80.0

    converted_to_feet = converter.convert(sample_length_meters, 'm', 'ft')
    converted_to_meters = converter.convert(sample_length_feet, 'ft', 'm')

    print(f"{sample_length_meters} meters is {converted_to_feet} feet")
    print(f"{sample_length_feet} feet is {converted_to_meters} meters")