class TimeConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self._validate()

    def _validate(self):
        valid_units = {"seconds", "minutes", "hours", "days"}
        if self.unit not in valid_units:
            raise ValueError(f"Invalid unit: {self.unit}. Must be one of {valid_units}")
        if not isinstance(self.value, (int, float)) or self.value < 0:
            raise ValueError("Value must be a non-negative number")

    def convert_all(self):
        seconds = self._to_seconds()
        return {
            "seconds": seconds,
            "minutes": seconds / 60,
            "hours": seconds / 3600,
            "days": seconds / 86400
        }

    def _to_seconds(self):
        if self.unit == "seconds":
            return self.value
        if self.unit == "minutes":
            return self.value * 60
        if self.unit == "hours":
            return self.value * 3600
        if self.unit == "days":
            return self.value * 86400
        return 0

    def convert_to(self, target_unit):
        seconds = self._to_seconds()
        if target_unit == "seconds":
            return seconds
        if target_unit == "minutes":
            return seconds / 60
        if target_unit == "hours":
            return seconds / 3600
        if target_unit == "days":
            return seconds / 86400
        raise ValueError(f"Invalid target unit: {target_unit}")

if __name__ == '__main__':
    sample_value = 2.5
    sample_unit = "hours"
    converter = TimeConverter(sample_value, sample_unit)
    result = converter.convert_all()
    print(result)
    specific_result = converter.convert_to("minutes")
    print(f"{sample_value} {sample_unit} is {specific_result} minutes")
    try:
        invalid_converter = TimeConverter(-5, "days")
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        converter.convert_to("years")
    except ValueError as e:
        print(f"Error caught: {e}")