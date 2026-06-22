class LengthConverter:
    def __init__(self):
        self.meters_to_feet = 3.28084
        self.feet_to_meters = 1.0 / self.meters_to_feet

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'm' and to_unit == 'ft':
            return value * self.meters_to_feet
        if from_unit == 'ft' and to_unit == 'm':
            return value * self.feet_to_meters
        if from_unit == 'meters' and to_unit == 'feet':
            return value * self.meters_to_feet
        if from_unit == 'feet' and to_unit == 'meters':
            return value * self.feet_to_meters
        if from_unit == 'meter' and to_unit == 'foot':
            return value * self.meters_to_feet
        if from_unit == 'foot' and to_unit == 'meter':
            return value * self.feet_to_meters
        raise ValueError("Unsupported units. Use 'm', 'ft', 'meter', 'meter', 'feet', 'foot'")

if __name__ == '__main__':
    converter = LengthConverter()
    result1 = converter.convert(10, 'm', 'ft')
    result2 = converter.convert(32.8084, 'ft', 'm')
    result3 = converter.convert(5, 'meter', 'feet')
    result4 = converter.convert(16.4042, 'foot', 'meter')
    print(result1)
    print(result2)
    print(result3)
    print(result4)