class LengthConverter:
    def __init__(self):
        self.meters_to_feet = 3.28084
        self.feet_to_meters = 1 / self.meters_to_feet

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        if from_unit == 'm' or from_unit == 'meter' or from_unit == 'meters':
            if to_unit == 'ft' or to_unit == 'feet' or to_unit == 'foot':
                return value * self.meters_to_feet
            else:
                raise ValueError(f"Unsupported target unit: {to_unit}")
        
        if from_unit == 'ft' or from_unit == 'foot' or from_unit == 'feet':
            if to_unit == 'm' or to_unit == 'meter' or to_unit == 'meters':
                return value * self.feet_to_meters
            else:
                raise ValueError(f"Unsupported target unit: {to_unit}")
        
        raise ValueError(f"Unsupported source unit: {from_unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    result1 = converter.convert(10, 'm', 'ft')
    result2 = converter.convert(52.5, 'ft', 'm')
    print(result1)
    print(result2)