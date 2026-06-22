class DistanceConverter:
    def __init__(self, value: float, unit: str) -> None:
        self._value = float(value)
        self._unit = unit.lower()
        if self._unit not in ("meters", "kilometers", "miles"):
            raise ValueError("Unit must be 'meters', 'kilometers', or 'miles'")

    @property
    def value(self) -> float:
        return self._value

    @property
    def unit(self) -> str:
        return self._unit

    def convert_to(self, target_unit: str) -> float:
        target_unit = target_unit.lower()
        if target_unit not in ("meters", "kilometers", "miles"):
            raise ValueError("Target unit must be 'meters', 'kilometers', or 'miles'")
        if self._unit == target_unit:
            return self._value
        
        if self._unit == "meters":
            if target_unit == "kilometers":
                return self._value / 1000
            if target_unit == "miles":
                return self._value / 1609.344
        elif self._unit == "kilometers":
            if target_unit == "meters":
                return self._value * 1000
            if target_unit == "miles":
                return self._value / 1.609344
        elif self._unit == "miles":
            if target_unit == "meters":
                return self._value * 1609.344
            if target_unit == "kilometers":
                return self._value * 1.609344
        return self._value

if __name__ == '__main__':
    converter = DistanceConverter(1.0, "kilometers")
    result = converter.convert_to("meters")
    print(result)
    result2 = converter.convert_to("miles")
    print(result2)