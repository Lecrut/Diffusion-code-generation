class LengthConverter:
    M_TO_FT = 3.28084
    FT_TO_M = 1 / M_TO_FT

    def convert(self, value, from_unit, to_unit):
        if from_unit == 'm' and to_unit == 'ft':
            return value * self.M_TO_FT
        elif from_unit == 'ft' and to_unit == 'm':
            return value * self.FT_TO_M
        else:
            raise ValueError('Unsupported unit conversion')

if __name__ == '__main__':
    converter = LengthConverter()
    
    sample_value_meters = 25.0
    sample_value_feet = 80.0
    
    converted_to_feet = converter.convert(sample_value_meters, 'm', 'ft')
    print(f"{sample_value_meters} meters is {converted_to_feet} feet")
    
    converted_to_meters = converter.convert(sample_value_feet, 'ft', 'm')
    print(f"{sample_value_feet} feet is {converted_to_meters} meters")