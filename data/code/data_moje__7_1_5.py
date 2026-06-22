class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._total_seconds = hours * 3600 + minutes * 60 + seconds

    @property
    def total_seconds(self):
        return self._total_seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        return cls(seconds=total_seconds)

    @classmethod
    def from_minutes(cls, total_minutes):
        return cls(minutes=total_minutes)

    @classmethod
    def from_hours(cls, total_hours):
        return cls(hours=total_hours)

    def to_hours(self):
        return self._total_seconds / 3600.0

    def to_minutes(self):
        return self._total_seconds / 60.0

    def to_seconds(self):
        return self._total_seconds

    def to_hms(self):
        total = int(self._total_seconds)
        hours, remainder = divmod(total, 3600)
        minutes, seconds = divmod(remainder, 60)
        return (hours, minutes, seconds)

    def add(self, other):
        if not isinstance(other, TimeConverter):
            raise TypeError("Unsupported operand type for add")
        return TimeConverter(total_seconds=self._total_seconds + other._total_seconds)

    def subtract(self, other):
        if not isinstance(other, TimeConverter):
            raise TypeError("Unsupported operand type for subtract")
        return TimeConverter(total_seconds=self._total_seconds - other._total_seconds)

    def multiply(self, factor):
        if not isinstance(factor, (int, float)):
            raise TypeError("Factor must be a number")
        return TimeConverter(total_seconds=self._total_seconds * factor)

    def divide(self, divisor):
        if not isinstance(divisor, (int, float)):
            raise TypeError("Divisor must be a number")
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return TimeConverter(total_seconds=self._total_seconds / divisor)

    def __eq__(self, other):
        if not isinstance(other, TimeConverter):
            return NotImplemented
        return self._total_seconds == other._total_seconds

    def __str__(self):
        h, m, s = self.to_hms()
        return f"{h}:{m:02d}:{s:02d}"

    def __repr__(self):
        return f"TimeConverter(total_seconds={self._total_seconds})"

if __name__ == '__main__':
    converter = TimeConverter(hours=2, minutes=30, seconds=45)
    print(converter)
    print(converter.to_hours())
    print(converter.to_minutes())
    print(converter.to_seconds())
    print(converter.to_hms())

    another = TimeConverter.from_seconds(9000)
    print(another)
    print(another.to_hms())

    added = converter.add(another)
    print(added)
    print(added.to_hms())

    subtracted = converter.subtract(TimeConverter.from_hours(1))
    print(subtracted)
    print(subtracted.to_hms())

    multiplied = converter.multiply(2)
    print(multiplied)
    print(multiplied.to_hms())

    divided = converter.divide(2)
    print(divided)
    print(divided.to_hms())