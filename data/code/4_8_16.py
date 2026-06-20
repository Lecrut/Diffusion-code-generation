class DistanceConverter:
    KM_TO_MILES = 0.621371
    MILES_TO_KM = 1.609344

    def __init__(self, distance, source_unit):
        self.distance = float(distance)
        self.source_unit = source_unit.lower()
        self._validate_unit(self.source_unit)

    def _validate_unit(self, unit):
        valid_units = ('km', 'kilometers', 'miles', 'mi')
        if unit not in valid_units:
            raise ValueError(f"Unsupported unit: {unit}")

    def convert_to_miles(self):
        if self.source_unit in ('km', 'kilometers'):
            return self.distance * self.KM_TO_MILES
        return self.distance

    def convert_to_km(self):
        if self.source_unit in ('miles', 'mi'):
            return self.distance * self.MILES_TO_KM
        return self.distance

    def convert(self, target_unit):
        target = target_unit.lower()
        if target in ('km', 'kilometers'):
            return self.convert_to_km()
        if target in ('miles', 'mi'):
            return self.convert_to_miles()
        raise ValueError(f"Unsupported target unit: {target_unit}")

def run_sample_conversions():
    converter_km = DistanceConverter(100, 'km')
    miles_result = converter_km.convert_to_miles()

    converter_mi = DistanceConverter(50, 'miles')
    km_result = converter_mi.convert_to_km()

    mixed_converter = DistanceConverter(25, 'kilometers')
    final_result = mixed_converter.convert('miles')

    return miles_result, km_result, final_result

if __name__ == '__main__':
    results = run_sample_conversions()
    print(results[0])
    print(results[1])
    print(results[2])