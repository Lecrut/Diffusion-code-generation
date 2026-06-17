class TimeConverter:
    def __init__(self, value: int = 0, unit: str = "seconds") -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer.")
        valid_units = {"seconds", "minutes", "hours", "days"}
        if unit.lower() not in valid_units:
            raise ValueError(f"Invalid time unit. Must be one of {valid_units}.")
        self.value = int(value)
        self.unit = unit.lower()
    def to_seconds(self, value: float | None = None) -> int:
        if value is not None and isinstance(value, (int, float)):
            return int(value * 60 ** {1: "minutes", 2: "hours", 3: "days"}.get(self.unit[0], 1))
    def convert_to_unit(self) -> dict[str, int]:
        return {
            "seconds": self.value * (60 ** {"minutes": 1, "hours": 2, "days": 3}.get("".join(c for c in self.unit if c.isdigit()), 0)),
        }
    def __str__(self) -> str:
        return f"{self.value} {self.unit}"
if __name__ == '__main__':
    tc = TimeConverter(3600, "seconds")
    print(tc.convert_to_unit())