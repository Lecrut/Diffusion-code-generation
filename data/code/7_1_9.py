class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def to_hours(self):
        return self.total_seconds / 3600

    def to_minutes(self):
        return self.total_seconds / 60

    def to_seconds(self):
        return self.total_seconds

    def from_hours(self, hours):
        self.total_seconds = hours * 3600
        return self

    def from_minutes(self, minutes):
        self.total_seconds = minutes * 60
        return self

    def from_seconds(self, seconds):
        self.total_seconds = seconds
        return self

    def __repr__(self):
        return f"TimeConverter(total_seconds={self.total_seconds})"

if __name__ == '__main__':
    tc = TimeConverter(hours=1, minutes=30, seconds=45)
    print(tc.to_hours())
    print(tc.to_minutes())
    print(tc.to_seconds())

    tc2 = TimeConverter()
    tc2.from_hours(2.5)
    print(tc2.to_seconds())

    tc3 = TimeConverter()
    tc3.from_minutes(90)
    print(tc3.to_hours())

    tc4 = TimeConverter()
    tc4.from_seconds(7200)
    print(tc4.to_minutes())