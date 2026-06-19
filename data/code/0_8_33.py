class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        meters_to_feet = 3.28084
        feet_to_meters = 1 / meters_to_feet
        
        if from_unit == 'meters' and to_unit == 'feet':
            return value * meters_to_feet
        elif from_unit == 'feet' and to_unit == 'meters':
            return value * feet_to_meters
        elif from_unit == to_unit:
            return value
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    converter = LengthConverter()
    
    result1 = converter.convert(1, 'meters', 'feet')
    print(result1)
    
    result2 = converter.convert(10, 'feet', 'meters')
    print(result2)
    
    result3 = converter.convert(5, 'meters', 'meters')
    print(result3)