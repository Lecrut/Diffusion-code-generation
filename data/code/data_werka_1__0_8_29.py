class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        meters = None
        if from_unit == 'meters':
            meters = value
        elif from_unit == 'feet':
            meters = value * 0.3048
        else:
            raise ValueError(f"Unknown from_unit: {from_unit}")

        if to_unit == 'meters':
            return meters
        elif to_unit == 'feet':
            return meters / 0.3048
        else:
            raise ValueError(f"Unknown to_unit: {to_unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    
    result1 = converter.convert(1, 'meters', 'feet')
    print(result1)
    
    result2 = converter.convert(1, 'feet', 'meters')
    print(result2)