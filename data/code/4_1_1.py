class DistanceConverter:
    METER = "meters"
    KILOMETER = "kilometers"
    MILE = "miles"

    CONVERSION_TO_METERS = {
        METER: 1.0,
        KILOMETER: 1000.0,
        MILE: 1609.344
    }

    def __init__(self):
        self.conversions = self.CONVERSION_TO_METERS

    def validate_unit(self, unit):
        if unit not in self.conversions:
            valid_units = ", ".join(self.conversions.keys())
            raise ValueError(f"Invalid unit '{unit}'. Valid units are: {valid_units}")

    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value must be numeric, got {type(value).__name__}")
        
        self.validate_unit(from_unit)
        self.validate_unit(to_unit)

        meters = value * self.conversions[from_unit]
        result = meters / self.conversions[to_unit]
        return round(result, 6)

    def meters_to_kilometers(self, meters):
        return self.convert(meters, self.METER, self.KILOMETER)

    def meters_to_miles(self, meters):
        return self.convert(meters, self.METER, self.MILE)

    def kilometers_to_meters(self, kilometers):
        return self.convert(kilometers, self.KILOMETER, self.METER)

    def kilometers_to_miles(self, kilometers):
        return self.convert(kilometers, self.KILOMETER, self.MILE)

    def miles_to_meters(self, miles):
        return self.convert(miles, self.MILE, self.METER)

    def miles_to_kilometers(self, miles):
        return self.convert(miles, self.MILE, self.KILOMETER)

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.meters_to_kilometers(1500))
    print(converter.kilometers_to_miles(5))
    print(converter.miles_to_meters(1))
    print(converter.convert(100, DistanceConverter.METER, DistanceConverter.MILE))
    print(converter.convert(2000, DistanceConverter.KILOMETER, DistanceConverter.METER))
    print(converter.convert(3, DistanceConverter.MILE, DistanceConverter.KILOMETER))