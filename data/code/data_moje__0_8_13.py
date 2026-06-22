class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        meters_per_foot = 0.3048
        
        if from_unit == 'meters':
            meters = value
        elif from_unit == 'feet':
            meters = value * meters_per_foot
        else:
            raise ValueError(f"Unknown from_unit: {from_unit}")
        
        if to_unit == 'meters':
            return meters
        elif to_unit == 'feet':
            return meters / meters_per_foot
        else:
            raise ValueError(f"Unknown to_unit: {to_unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    result1 = converter.convert(10, 'meters', 'feet')
    print(result1)
    
    result2 = converter.convert(10, 'feet', 'meters')
    print(result2)
    
    result3 = converter.convert(1, 'meters', 'meters')
    print(result3)
    
    result4 = converter.convert(1, 'feet', 'feet')
    print(result4)