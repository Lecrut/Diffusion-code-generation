class LengthConverter:
    METERS_TO_FEET = 3.280839895
    FEET_TO_METERS = 0.3048

    def convert(self, value, from_unit, to_unit):
        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()

        if from_unit_lower == 'm':
            if to_unit_lower == 'm':
                return value
            elif to_unit_lower == 'ft' or to_unit_lower == 'feet':
                return value * self.METERS_TO_FEET
            else:
                raise ValueError(f"Unsupported target unit: {to_unit}")
        elif from_unit_lower == 'ft' or from_unit_lower == 'feet':
            if to_unit_lower == 'ft' or to_unit_lower == 'feet':
                return value
            elif to_unit_lower == 'm':
                return value * self.FEET_TO_METERS
            else:
                raise ValueError(f"Unsupported target unit: {to_unit}")
        else:
            raise ValueError(f"Unsupported source unit: {from_unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    result1 = converter.convert(10, 'm', 'ft')
    print(result1)
    result2 = converter.convert(5.5, 'ft', 'm')
    print(result2)
    result3 = converter.convert(100, 'm', 'm')
    print(result3)