class DistanceConverter:
    MILES = "miles"
    KILOMETERS = "kilometers"
    METERS = "meters"

    METERS_PER_MILE = 1609.344
    METERS_PER_KILOMETER = 1000.0
    METERS_PER_METER = 1.0

    def __init__(self):
        self._unit_to_meters = {
            self.MILES: self.METERS_PER_MILE,
            self.KILOMETERS: self.METERS_PER_KILOMETER,
            self.METERS: self.METERS_PER_METER
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self._unit_to_meters:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self._unit_to_meters:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        
        meters = value * self._unit_to_meters[from_unit]
        result = meters / self._unit_to_meters[to_unit]
        return result

if __name__ == '__main__':
    converter = DistanceConverter()
    miles_to_kms = converter.convert(10, DistanceConverter.MILES, DistanceConverter.KILOMETERS)
    kms_to_meters = converter.convert(5, DistanceConverter.KILOMETERS, DistanceConverter.METERS)
    meters_to_miles = converter.convert(1609.344, DistanceConverter.METERS, DistanceConverter.MILES)
    print(miles_to_kms)
    print(kms_to_meters)
    print(meters_to_miles)