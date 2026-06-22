class TimeConverter:
    def __init__(self, value, from_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise ValueError("Value must be non-negative")
        
        self.units = {
            "nanosecond": 1e-9,
            "microsecond": 1e-6,
            "millisecond": 1e-3,
            "second": 1,
            "minute": 60,
            "hour": 3600,
            "day": 86400,
            "week": 604800,
            "month": 2592000,
            "year": 31536000
        }
        
        from_unit_lower = from_unit.lower()
        if from_unit_lower not in self.units:
            raise ValueError(f"Unknown unit: {from_unit}")
        
        self.value = value
        self.from_unit = from_unit_lower

    def _get_base_seconds(self):
        return self.value * self.units[self.from_unit]

    def convert(self, to_unit):
        to_unit_lower = to_unit.lower()
        if to_unit_lower not in self.units:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        base_seconds = self._get_base_seconds()
        result = base_seconds / self.units[to_unit_lower]
        
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result

    def to_seconds(self):
        return self._get_base_seconds()

    def to_minutes(self):
        return self.convert("minute")

    def to_hours(self):
        return self.convert("hour")

    def to_days(self):
        return self.convert("day")

if __name__ == '__main__':
    converter = TimeConverter(3661, "second")
    print(converter.to_hours())
    print(converter.to_days())
    print(converter.to_minutes())