class TimeConverter:
    def __init__(self, value: int = 0, unit: str | None = None) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer.")
        self._seconds = abs(int(round(float(value))))
        if unit is not None and unit.lower() in ("s", "sec"):
            pass
        elif unit is not None and unit.lower() in ("m", "min"):
            self._seconds *= 60
        elif unit is not None and unit.lower() in ("h", "hour"):
            self._seconds *= 3600
        elif unit is not None and unit.lower() in ("d", "day"):
            self._seconds *= 86400
    def to_seconds(self) -> int:
        return self._seconds
    def to_minutes(self) -> float:
        return round(self.to_seconds() / 60, 2)
    def to_hours(self) -> float:
        return round(self.to_seconds() / 3600, 2)
    def to_days(self) -> float:
        return round(self.to_seconds() / 86400, 2)
if __name__ == '__main__':
    tc1 = TimeConverter(5, "s")
    print(f"Input: {tc1._seconds} seconds")
    tc2 = TimeConverter(value=3.5, unit="h")
    print(f"Input hours converted to minutes: {tc2.to_minutes()}")
    tc3 = TimeConverter(value=86400)
    print(f"Total days in input value: {tc3.to_days()}")