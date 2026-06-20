class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self._total_seconds = total_seconds

    @property
    def total_seconds(self):
        return self._total_seconds

    @property
    def hours(self):
        return self._total_seconds // 3600

    @property
    def minutes(self):
        return (self._total_seconds // 60) % 60

    @property
    def seconds(self):
        return self._total_seconds % 60

    def to_hours(self):
        return self._total_seconds / 3600.0

    def to_minutes(self):
        return self._total_seconds / 60.0

    def to_seconds(self):
        return self._total_seconds

    def __repr__(self):
        h = self.hours
        m = self.minutes
        s = self.seconds
        return f"{h:02d}:{m:02d}:{s:02d}"

if __name__ == '__main__':
    tc = TimeConverter(hours=2, minutes=30, seconds=45)
    print(f"Total Seconds: {tc.total_seconds}")
    print(f"Hours: {tc.hours}, Minutes: {tc.minutes}, Seconds: {tc.seconds}")
    print(f"Decimal Hours: {tc.to_hours()}")
    print(f"Decimal Minutes: {tc.to_minutes()}")
    print(f"Formatted Time: {tc}")