import math

class TimeConverter:
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_DAY = 86400

    def __init__(self, value, unit):
        valid_units = ["seconds", "minutes", "hours", "days"]
        if unit not in valid_units:
            raise ValueError(f"Invalid unit: {unit}. Must be one of {valid_units}")
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        self.original_value = float(value)
        self.original_unit = unit
        self.total_seconds = self._to_seconds()

    def _to_seconds(self):
        if self.original_unit == "seconds":
            return self.original_value
        elif self.original_unit == "minutes":
            return self.original_value * self.SECONDS_PER_MINUTE
        elif self.original_unit == "hours":
            return self.original_value * self.SECONDS_PER_HOUR
        elif self.original_unit == "days":
            return self.original_value * self.SECONDS_PER_DAY

    def convert(self):
        results = {
            "seconds": self.total_seconds,
            "minutes": self.total_seconds / self.SECONDS_PER_MINUTE,
            "hours": self.total_seconds / self.SECONDS_PER_HOUR,
            "days": self.total_seconds / self.SECONDS_PER_DAY
        }
        return results

    def __str__(self):
        results = self.convert()
        lines = []
        lines.append(f"Original: {self.original_value} {self.original_unit}")
        for unit, value in results.items():
            if value >= 1:
                lines.append(f"{unit.capitalize()}: {value}")
            else:
                lines.append(f"{unit.capitalize()}: {value}")
        return "\n".join(lines)

def run_conversion(value, unit):
    converter = TimeConverter(value, unit)
    return converter.convert()

if __name__ == "__main__":
    sample_value = 2.5
    sample_unit = "hours"
    result = run_conversion(sample_value, sample_unit)
    print(f"Input: {sample_value} {sample_unit}")
    for unit, val in result.items():
        print(f"{unit}: {val}")