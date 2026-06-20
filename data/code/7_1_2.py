class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self._total_seconds = total_seconds

    @property
    def hours(self):
        return self._total_seconds // 3600

    @property
    def minutes(self):
        return (self._total_seconds % 3600) // 60

    @property
    def seconds(self):
        return self._total_seconds % 60

    def to_seconds(self):
        return self._total_seconds

    def to_minutes(self):
        return self._total_seconds / 60

    def to_hours(self):
        return self._total_seconds / 3600

    @classmethod
    def from_seconds(cls, total_seconds):
        return cls(seconds=total_seconds)

    @classmethod
    def from_minutes(cls, total_minutes):
        return cls(minutes=total_minutes)

    @classmethod
    def from_hours(cls, total_hours):
        return cls(hours=total_hours)

    def __repr__(self):
        return f"TimeConverter(hours={self.hours}, minutes={self.minutes}, seconds={self.seconds})"

if __name__ == '__main__':
    tc = TimeConverter(hours=2, minutes=30, seconds=45)
    print(tc.to_seconds())
    print(tc.to_minutes())
    print(tc.to_hours())
    print(repr(tc))

    tc2 = TimeConverter.from_seconds(5000)
    print(repr(tc2))
    print(tc2.to_minutes())