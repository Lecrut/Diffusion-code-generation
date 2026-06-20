class LengthConverter:
    METERS_PER_FOOT = 0.3048

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit == 'meter' or from_unit == 'meters' or from_unit == 'm':
            meters = value
        elif from_unit == 'foot' or from_unit == 'feet' or from_unit == 'ft':
            meters = value * self.METERS_PER_FOOT
        else:
            raise ValueError("Invalid from_unit")

        if to_unit == 'meter' or to_unit == 'meters' or to_unit == 'm':
            return meters
        elif to_unit == 'foot' or to_unit == 'feet' or to_unit == 'ft':
            return meters / self.METERS_PER_FOOT
        else:
            raise ValueError("Invalid to_unit")

if __name__ == '__main__':
    converter = LengthConverter()
    result1 = converter.convert(10, 'meters', 'feet')
    print(result1)
    result2 = converter.convert(5, 'feet', 'meters')
    print(result2)