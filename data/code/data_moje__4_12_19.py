class DistanceConverter:
    MILE_TO_KM = 1.60934
    METER_TO_KM = 0.001
    MILE_TO_METER = 1609.34
    KM_TO_METER = 1000
    KM_TO_MILE = 1 / MILE_TO_KM
    METER_TO_MILE = 1 / MILE_TO_METER

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        normalized = self._to_kilometers(value, from_unit)
        return self._from_kilometers(normalized, to_unit)

    def _to_kilometers(self, value, unit):
        if unit == 'mile':
            return value * self.MILE_TO_KM
        elif unit == 'kilometer':
            return value
        elif unit == 'meter':
            return value * self.METER_TO_KM
        else:
            raise ValueError(f"Unknown unit: {unit}")

    def _from_kilometers(self, value, unit):
        if unit == 'mile':
            return value * self.KM_TO_MILE
        elif unit == 'kilometer':
            return value
        elif unit == 'meter':
            return value / self.METER_TO_KM
        else:
            raise ValueError(f"Unknown unit: {unit}")

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1, 'mile', 'kilometer'))
    print(converter.convert(1, 'kilometer', 'mile'))
    print(converter.convert(1, 'mile', 'meter'))
    print(converter.convert(1, 'meter', 'mile'))
    print(converter.convert(1, 'kilometer', 'meter'))
    print(converter.convert(1, 'meter', 'kilometer'))
    print(converter.convert(5, 'mile', 'kilometer'))
    print(converter.convert(100, 'meter', 'kilometer'))