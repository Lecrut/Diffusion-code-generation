class DistanceConverter:
    MILE_TO_KM = 1.60934
    KM_TO_METER = 1000.0
    MILE_TO_METER = MILE_TO_KM * KM_TO_METER

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.upper()

    def _to_meters(self):
        if self.unit == 'MILE':
            return self.value * self.MILE_TO_METER
        elif self.unit == 'KM':
            return self.value * self.KM_TO_METER
        elif self.unit == 'METER':
            return self.value
        else:
            raise ValueError(f"Unsupported unit: {self.unit}")

    def convert_to(self, target_unit):
        target_unit = target_unit.upper()
        meters = self._to_meters()
        if target_unit == 'MILE':
            return meters / self.MILE_TO_METER
        elif target_unit == 'KM':
            return meters / self.KM_TO_METER
        elif target_unit == 'METER':
            return meters
        else:
            raise ValueError(f"Unsupported target unit: {target_unit}")

if __name__ == '__main__':
    d1 = DistanceConverter(1, 'mile')
    print(d1.convert_to('km'))
    print(d1.convert_to('meter'))

    d2 = DistanceConverter(1000, 'meter')
    print(d2.convert_to('mile'))
    print(d2.convert_to('km'))

    d3 = DistanceConverter(5, 'km')
    print(d3.convert_to('mile'))
    print(d3.convert_to('meter'))