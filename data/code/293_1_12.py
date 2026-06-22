class DistanceConverter:
    conversion_factors = {('km', 'mi'): 0.621371, ('mi', 'km'): 1 / 0.621371}

    @staticmethod
    def convert(value, from_unit, to_unit):
        if (from_unit, to_unit) in DistanceConverter.conversion_factors:
            return value * DistanceConverter.conversion_factors[from_unit, to_unit]
        else:
            raise ValueError(f'Unsupported conversion: {from_unit} to {to_unit}')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'km', 'mi'))
    print(converter.convert(5, 'mi', 'km'))