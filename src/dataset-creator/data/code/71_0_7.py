class TimeConverter:
    def __init__(self, seconds=None):
        if isinstance(seconds, int) and seconds >= 0:
            self.total_seconds = seconds
        else:
            raise ValueError("Input must be a non-negative integer.")
    @classmethod
    def from_minutes(cls, minutes):
        if not isinstance(minutes, int) or minutes < 0:
            raise ValueError("Minutes must be a non-negative integer.")
        return cls(seconds=minutes * 60)
    @classmethod
    def from_hours(cls, hours):
        if not isinstance(hours, int) or hours < 0:
            raise ValueError("Hours must be a non-negative integer.")
        return cls(seconds=hours * 3600)
    @classmethod
    def from_days(cls, days):
        if not isinstance(days, int) or days < 0:
            raise ValueError("Days must be a non-negative integer.")
        return cls(seconds=days * 86400)
    def to_minutes(self):
        return self.total_seconds // 60
    def to_hours(self):
        return self.total_seconds // 3600
    def to_days(self):
        return self.total_seconds // 86400
if __name__ == '__main__':
    t1 = TimeConverter(seconds=7200)
    print(f"Seconds: {t1.to_minutes()} minutes, {t1.to_hours()} hours")
    t2 = TimeConverter.from_days(3)
    print(f"Days 3 converted to seconds: {t2.total_seconds}")