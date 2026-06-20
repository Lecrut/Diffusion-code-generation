class DistanceConverter:
    MILES_TO_KM = 1.60934
    KM_TO_MILES = 1 / MILES_TO_KM
    METERS_PER_KM = 1000
    METERS_PER_MILE = MILES_TO_KM * METERS_PER_KM
    KM_PER_METER = 1 / METERS_PER_KM
    MILES_PER_METER = KM_PER_METER * KM_TO_MILES

    UNITS = ('miles', 'kilometers', 'meters')

    def __init__(self):
        self.conversion_matrix = self._build_matrix()

    def _build_matrix(self):
        matrix = {}
        for unit in self.UNITS:
            matrix[unit] = {}
            for target_unit in self.UNITS:
                matrix[unit][target_unit] = self._get_factor(unit, target_unit)
        return matrix

    def _get_factor(self, from_unit, to_unit):
        if from_unit == to_unit:
            return 1.0
        if from_unit == 'miles':
            if to_unit == 'kilometers':
                return self.MILES_TO_KM
            return self.METERS_PER_MILE
        if from_unit == 'kilometers':
            if to_unit == 'miles':
                return self.KM_TO_MILES
            return self.METERS_PER_KM
        if from_unit == 'meters':
            if to_unit == 'miles':
                return self.MILES_PER_METER
            return self.KM_PER_METER
        raise ValueError("Unknown unit")

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_matrix:
            raise ValueError(f"Invalid from_unit: {from_unit}")
        if to_unit not in self.conversion_matrix[from_unit]:
            raise ValueError(f"Invalid to_unit: {to_unit}")
        factor = self.conversion_matrix[from_unit][to_unit]
        return value * factor

if __name__ == '__main__':
    converter = DistanceConverter()
    miles = 10
    km = converter.convert(miles, 'miles', 'kilometers')
    print(f"{miles} miles = {km} kilometers")
    meters = converter.convert(km, 'kilometers', 'meters')
    print(f"{km} kilometers = {meters} meters")
    back_to_miles = converter.convert(meters, 'meters', 'miles')
    print(f"{meters} meters = {back_to_miles} miles")