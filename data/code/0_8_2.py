class LengthConverter:
    METERS_PER_FOOT = 0.3048
    FEET_PER_METER = 1 / METERS_PER_FOOT

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        if from_unit == 'meters' and to_unit == 'feet':
            return value * self.FEET_PER_METER
        elif from_unit == 'feet' and to_unit == 'meters':
            return value * self.METERS_PER_FOOT
        else:
            raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    result = converter.convert(10, 'meters', 'feet')
    print(result)
    result2 = converter.convert(32.808399, 'feet', 'meters')
    print(result2)