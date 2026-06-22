class LengthConverter:
    def convert(self, value, from_unit, to_unit):
        meters = 0.0
        if from_unit == 'meters':
            meters = value
        elif from_unit == 'feet':
            meters = value * 0.3048
        else:
            raise ValueError(f"Unknown unit: {from_unit}")

        result = 0.0
        if to_unit == 'meters':
            result = meters
        elif to_unit == 'feet':
            result = meters / 0.3048
        else:
            raise ValueError(f"Unknown unit: {to_unit}")

        return result

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1, 'meters', 'feet'))
    print(converter.convert(1, 'feet', 'meters'))