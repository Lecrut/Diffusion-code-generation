class DistanceConverter:
    METER_TO_KILOMETER = 0.001
    METER_TO_CENTIMETER = 100.0
    METER_TO_MILLIMETER = 1000.0
    METER_TO_INCH = 39.3701
    METER_TO_FOOT = 3.28084
    METER_TO_YARD = 1.09361
    METER_TO_MILE = 0.000621371

    @staticmethod
    def convert(value, from_unit, to_unit):
        conversion_factors = {'m': 1.0, 'km': DistanceConverter.METER_TO_KILOMETER, 'cm': DistanceConverter.METER_TO_CENTIMETER, 'mm': DistanceConverter.METER_TO_MILLIMETER, 'in': DistanceConverter.METER_TO_INCH, 'ft': DistanceConverter.METER_TO_FOOT, 'yd': DistanceConverter.METER_TO_YARD, 'mi': DistanceConverter.METER_TO_MILE}
        if from_unit not in conversion_factors:
            raise ValueError(f'Unsupported unit: {from_unit}')
        if to_unit not in conversion_factors:
            raise ValueError(f'Unsupported unit: {to_unit}')
        factor_from = conversion_factors[from_unit]
        factor_to = conversion_factors[to_unit]
        return value * factor_from / factor_to
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'm', 'km'))
    print(converter.convert(25.4, 'cm', 'in'))
    print(converter.convert(100, 'yd', 'm'))
    print(converter.convert(5, 'mi', 'km'))