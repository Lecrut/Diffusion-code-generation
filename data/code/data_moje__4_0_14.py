class DistanceUnitConverter:
    METER_TO_KILOMETER = 0.001
    METER_TO_MILE = 0.000621371

    def __init__(self, value: float, unit: str):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number")
        if value < 0:
            raise ValueError("Value must be non-negative")
        valid_units = {"m", "km", "mi", "meters", "kilometers", "miles"}
        if unit.lower() not in valid_units:
            raise ValueError("Unit must be 'm', 'km', or 'mi'")
        self.value = float(value)
        self.unit = unit.lower()

    def _to_meters(self) -> float:
        if self.unit in ("m", "meters"):
            return self.value
        if self.unit in ("km", "kilometers"):
            return self.value * 1000
        if self.unit in ("mi", "miles"):
            return self.value / self.METER_TO_MILE
        return 0.0

    def convert(self, target_unit: str) -> float:
        if target_unit is None:
            raise ValueError("Target unit cannot be None")
        if not isinstance(target_unit, str):
            raise ValueError("Target unit must be a string")
        valid_targets = {"m", "km", "mi"}
        target_short = target_unit.lower()
        if target_short not in valid_targets:
            raise ValueError("Target unit must be 'm', 'km', or 'mi'")
        meters = self._to_meters()
        if target_short in ("m", "meters"):
            return meters
        if target_short in ("km", "kilometers"):
            return meters * self.METER_TO_KILOMETER
        if target_short in ("mi", "miles"):
            return meters * self.METER_TO_MILE
        return 0.0

if __name__ == "__main__":
    converter_m = DistanceUnitConverter(1609.34, "m")
    result_km = converter_m.convert("km")
    print(result_km)
    converter_mi = DistanceUnitConverter(1, "mi")
    result_m = converter_mi.convert("m")
    print(result_m)
    converter_km = DistanceUnitConverter(5, "km")
    result_mi = converter_km.convert("mi")
    print(result_mi)