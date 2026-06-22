class LengthConverter:
    FEET_PER_METER = 3.280839895013123

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit == to_unit:
            return value
        if from_unit == 'meters' and to_unit == 'feet':
            return value * self.FEET_PER_METER
        if from_unit == 'feet' and to_unit == 'meters':
            return value / self.FEET_PER_METER
        raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    converter = LengthConverter()
    result1 = converter.convert(1.0, 'meters', 'feet')
    result2 = converter.convert(3.280839895013123, 'feet', 'meters')
    print(result1)
    print(result2)