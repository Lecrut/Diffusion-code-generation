class DistanceConverter:
    METER_TO_KM = 0.001
    METER_TO_MILE = 0.000621371

    def __init__(self, value, unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number")
        if unit not in ['m', 'km', 'mi']:
            raise ValueError("Unit must be 'm', 'km', or 'mi'")
        self.value = float(value)
        self.unit = unit.lower()

    def to_meters(self):
        if self.unit == 'm':
            return self.value
        elif self.unit == 'km':
            return self.value / DistanceConverter.METER_TO_KM
        elif self.unit == 'mi':
            return self.value / DistanceConverter.METER_TO_MILE

    def to_kilometers(self):
        if self.unit == 'km':
            return self.value
        elif self.unit == 'm':
            return self.value * DistanceConverter.METER_TO_KM
        elif self.unit == 'mi':
            return (self.value / DistanceConverter.METER_TO_MILE) * DistanceConverter.METER_TO_KM

    def to_miles(self):
        if self.unit == 'mi':
            return self.value
        elif self.unit == 'm':
            return self.value * DistanceConverter.METER_TO_MILE
        elif self.unit == 'km':
            return (self.value / DistanceConverter.METER_TO_KM) * DistanceConverter.METER_TO_MILE

if __name__ == '__main__':
    converter_meters = DistanceConverter(1000, 'm')
    print(converter_meters.to_kilometers())
    print(converter_meters.to_miles())
    converter_km = DistanceConverter(5, 'km')
    print(converter_km.to_meters())
    print(converter_km.to_miles())
    converter_miles = DistanceConverter(10, 'mi')
    print(converter_miles.to_meters())
    print(converter_miles.to_kilometers())