class LengthConverter:
    METERS_PER_FOOT = 0.3048

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit.lower() == 'meters':
            if to_unit.lower() == 'feet':
                return value / self.METERS_PER_FOOT
            else:
                raise ValueError("Unsupported target unit")
        elif from_unit.lower() == 'feet':
            if to_unit.lower() == 'meters':
                return value * self.METERS_PER_FOOT
            else:
                raise ValueError("Unsupported target unit")
        else:
            raise ValueError("Unsupported source unit")

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1.0, 'meters', 'feet'))
    print(converter.convert(1.0, 'feet', 'meters'))