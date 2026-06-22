class DistanceConverter:
    CONVERSION_FACTORS = {
        ('km', 'miles'): 0.621371,
        ('miles', 'km'): 1.60934,
        ('km', 'meters'): 1000,
        ('meters', 'km'): 0.001,
        ('miles', 'meters'): 1609.34,
        ('meters', 'miles'): 0.000621371
    }

    @staticmethod
    def convert(distance, source_unit, target_unit):
        if source_unit == target_unit:
            return distance
        key = (source_unit, target_unit)
        if key in DistanceConverter.CONVERSION_FACTORS:
            factor = DistanceConverter.CONVERSION_FACTORS[key]
            return distance * factor
        else:
            raise ValueError(f"Unsupported conversion from {source_unit} to {target_unit}")

if __name__ == '__main__':
    converter = DistanceConverter()
    try:
        miles_to_cm = converter.convert(1, 'miles', 'cm')
        print(miles_to_cm)
    except ValueError as e:
        print(e)