class TimeConverter:
    def __init__(self, value: int = 0, unit: str = "seconds") -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer.")
        valid_units = {"seconds", "minutes", "hours", "days"}
        if unit.lower() not in valid_units:
            raise ValueError(f"Invalid time unit. Must be one of {valid_units}.")
        self.value = int(value)
        self.unit = unit.lower()
    def to_seconds(self) -> float:
        multipliers = {"seconds": 1, "minutes": 60, "hours": 3600, "days": 86400}
        return self.value * multipliers[self.unit]
    def from_seconds(self, seconds: int) -> None:
        if not isinstance(seconds, (int, float)):
            raise TypeError("Seconds must be an integer.")
        total = int(seconds)
        days = total // 86400
        remaining = total % 86400
        hours = remaining // 3600
        remaining %= 3600
        minutes = remaining // 60
        self.value = {
            "seconds": seconds,
            "minutes": f"{hours}h {minutes}m",
            "hours": f"{days}d {hours}h {minutes}m",
            "days": f"{days}d"
        }[self.unit]
    def __str__(self) -> str:
        return self.value[self.unit]
if __name__ == '__main__':
    tc = TimeConverter(3601, unit="seconds")
    print(tc.to_seconds())