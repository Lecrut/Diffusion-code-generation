class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.total_seconds = total_seconds

    def to_seconds(self):
        return self.total_seconds

    def to_minutes(self):
        return self.total_seconds / 60

    def to_hours(self):
        return self.total_seconds / 3600

    def from_seconds(self, seconds):
        self.total_seconds = seconds
        return self

    def from_minutes(self, minutes):
        self.total_seconds = minutes * 60
        return self

    def from_hours(self, hours):
        self.total_seconds = hours * 3600
        return self

    def __repr__(self):
        return f"TimeConverter(total_seconds={self.total_seconds})"

if __name__ == '__main__':
    converter = TimeConverter(hours=2, minutes=30, seconds=45)
    print(converter.to_seconds())
    print(converter.to_minutes())
    print(converter.to_hours())

    converter.from_minutes(90)
    print(converter.to_seconds())
    print(converter.to_hours())

    converter.from_hours(1.5)
    print(converter.to_minutes())
    print(converter.to_seconds())