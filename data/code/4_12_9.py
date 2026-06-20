class DistanceConverter:
    MILE_TO_KILOMETER = 1.60934
    MILE_TO_METER = 1609.34
    KILOMETER_TO_METER = 1000

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()

    def _to_meters(self):
        if self.unit == 'miles':
            return self.value * self.MILE_TO_METER
        elif self.unit == 'kilometers':
            return self.value * self.KILOMETER_TO_METER
        elif self.unit == 'meters':
            return self.value
        else:
            raise ValueError(f"Unsupported unit: {self.unit}")

    def convert(self, target_unit):
        target_unit = target_unit.lower()
        if target_unit not in ['miles', 'kilometers', 'meters']:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        base_value = self._to_meters()
        
        if target_unit == 'meters':
            return base_value
        elif target_unit == 'kilometers':
            return base_value / self.KILOMETER_TO_METER
        elif target_unit == 'miles':
            return base_value / self.MILE_TO_METER

if __name__ == '__main__':
    converter = DistanceConverter(5, 'miles')
    result_km = converter.convert('kilometers')
    result_m = converter.convert('meters')
    print(result_km)
    print(result_m)