class DistanceConverter:
    MILE_TO_KM = 1.609344
    MILE_TO_METER = 1609.344
    KM_TO_METER = 1000.0

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        if from_unit == 'miles':
            if to_unit == 'kilometers':
                return value * cls.MILE_TO_KM
            elif to_unit == 'meters':
                return value * cls.MILE_TO_METER
        elif from_unit == 'kilometers':
            if to_unit == 'miles':
                return value / cls.MILE_TO_KM
            elif to_unit == 'meters':
                return value * cls.KM_TO_METER
        elif from_unit == 'meters':
            if to_unit == 'miles':
                return value / cls.MILE_TO_METER
            elif to_unit == 'kilometers':
                return value / cls.KM_TO_METER

        raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1, 'miles', 'kilometers'))
    print(converter.convert(1, 'kilometers', 'meters'))
    print(converter.convert(1609.344, 'meters', 'miles'))
    print(converter.convert(5, 'miles', 'meters'))
    print(converter.convert(10, 'kilometers', 'miles'))