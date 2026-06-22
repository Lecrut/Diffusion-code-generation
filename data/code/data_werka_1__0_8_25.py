class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        meters = 0.0
        if from_unit == 'meters':
            meters = value
        elif from_unit == 'feet':
            meters = value * 0.3048
        else:
            raise ValueError(f"Unknown from_unit: {from_unit}")

        result = 0.0
        if to_unit == 'meters':
            result = meters
        elif to_unit == 'feet':
            result = meters / 0.3048
        else:
            raise ValueError(f"Unknown to_unit: {to_unit}")
        
        return result

if __name__ == '__main__':
    converter = LengthConverter()
    
    feet_to_meters = converter.convert(10, 'feet', 'meters')
    print(feet_to_meters)
    
    meters_to_feet = converter.convert(5, 'meters', 'feet')
    print(meters_to_feet)