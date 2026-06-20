class DistanceConverter:
    METER_TO_KM = 0.001
    METER_TO_MILE = 0.000621371
    KM_TO_METER = 1000
    MILE_TO_METER = 1609.344

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self._validate_unit(unit)

    def _validate_unit(self, unit):
        valid_units = ["m", "km", "mi", "meter", "kilometer", "mile", "meters", "kilometers", "miles"]
        if unit not in valid_units:
            raise ValueError(f"Invalid unit: {unit}")

    def _to_meters(self):
        unit = self.unit.lower()
        if unit.startswith("m") and unit != "mi":
            return self.value
        elif unit.startswith("k") or unit == "kilometer":
            return self.value * self.KM_TO_METER
        else:
            return self.value * self.MILE_TO_METER

    def convert_to_kilometers(self):
        meters = self._to_meters()
        return meters * self.METER_TO_KM

    def convert_to_miles(self):
        meters = self._to_meters()
        return meters * self.METER_TO_MILE

    def convert_to_meters(self):
        return self._to_meters()

if __name__ == "__main__":
    converter1 = DistanceConverter(5, "km")
    print(converter1.convert_to_miles())
    
    converter2 = DistanceConverter(1000, "m")
    print(converter2.convert_to_kilometers())
    
    converter3 = DistanceConverter(26.2, "mi")
    print(converter3.convert_to_meters())