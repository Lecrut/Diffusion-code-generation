class UnitConverter:
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        conversion_factors = {
            'meters': 1,
            'kilometers': 1000,
            'miles': 1609.34,
            'feet': 0.3048,
            'inches': 0.0254
        }
        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            raise ValueError("Unsupported unit provided.")
        meters = value
        if from_unit != 'meters':
            if from_unit == 'kilometers':
                meters = value * 1000
            elif from_unit == 'miles':
                meters = value * 1609.34
            elif from_unit == 'feet':
                meters = value * 0.3048
            elif from_unit == 'inches':
                meters = value * 0.0254
        if to_unit != 'meters':
            if to_unit == 'kilometers':
                return meters / 1000
            elif to_unit == 'miles':
                return meters / 1609.34
            elif to_unit == 'feet':
                return meters / 0.3048
            elif to_unit == 'inches':
                return meters / 0.0254
        return meters
if __name__ == '__main__':
    converter = UnitConverter()
    value1 = 10
    from_unit1 = 'kilometers'
    to_unit1 = 'miles'
    result1 = converter.convert(value1, from_unit1, to_unit1)
    print(f"{value1} {from_unit1} is equal to {result1:.2f} {to_unit1}")
    value2 = 5000
    from_unit2 = 'meters'
    to_unit2 = 'feet'
    result2 = converter.convert(value2, from_unit2, to_unit2)
    print(f"{value2} {from_unit2} is equal to {result2:.2f} {to_unit2}")
    value3 = 10
    from_unit3 = 'miles'
    to_unit3 = 'feet'
    result3 = converter.convert(value3, from_unit3, to_unit3)
    print(f"{value3} {from_unit3} is equal to {result3:.2f} {to_unit3}")
    value4 = 1000
    from_unit4 = 'meters'
    to_unit4 = 'kilometers'
    result4 = converter.convert(value4, from_unit4, to_unit4)
    print(f"{value4} {from_unit4} is equal to {result4:.2f} {to_unit4}")