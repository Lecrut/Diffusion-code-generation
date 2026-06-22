class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            ('miles', 'cm'): 160934 * 100
        }

    def convert(self, distance, source_unit, target_unit):
        if source_unit == target_unit:
            return distance
        key = (source_unit, target_unit)
        if key in self.conversion_factors:
            factor = self.conversion_factors[key]
            return distance * factor
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1, 'miles', 'cm'))