class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'meter' and to_unit == 'foot':
            return value * 3.28084
        if from_unit == 'foot' and to_unit == 'meter':
            return value / 3.28084
        if from_unit == 'meters' and to_unit == 'feet':
            return value * 3.28084
        if from_unit == 'feet' and to_unit == 'meters':
            return value / 3.28084
        raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    result1 = converter.convert(1, 'meter', 'foot')
    result2 = converter.convert(100, 'foot', 'meter')
    result3 = converter.convert(5.5, 'meters', 'feet')
    print(result1)
    print(result2)
    print(result3)