class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def to_hours(self):
        return self.total_seconds / 3600

    def to_minutes(self):
        return self.total_seconds / 60

    def to_seconds(self):
        return self.total_seconds

    @staticmethod
    def from_hours(hours):
        total_sec = hours * 3600
        return TimeConverter(seconds=total_sec)

    @staticmethod
    def from_minutes(minutes):
        total_sec = minutes * 60
        return TimeConverter(seconds=total_sec)

    @staticmethod
    def from_seconds(seconds):
        return TimeConverter(seconds=seconds)

if __name__ == '__main__':
    converter = TimeConverter(hours=1, minutes=30, seconds=45)
    print(converter.to_hours())
    print(converter.to_minutes())
    print(converter.to_seconds())
    from_hours = TimeConverter.from_hours(2.5)
    print(from_hours.to_minutes())
    from_minutes = TimeConverter.from_minutes(90)
    print(from_minutes.to_seconds())
    from_seconds = TimeConverter.from_seconds(3661)
    print(from_seconds.to_hours())