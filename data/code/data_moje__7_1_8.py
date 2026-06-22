class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

    def to_hours(self):
        return self.total_seconds / 3600

    def to_minutes(self):
        return self.total_seconds / 60

    def to_seconds(self):
        return self.total_seconds

    def to_dhms(self):
        remaining = self.total_seconds
        hours = remaining // 3600
        remaining %= 3600
        minutes = remaining // 60
        seconds = remaining % 60
        return int(hours), int(minutes), int(seconds)

    @staticmethod
    def from_hours(hours):
        return TimeConverter(hours=hours)

    @staticmethod
    def from_minutes(minutes):
        return TimeConverter(minutes=minutes)

    @staticmethod
    def from_seconds(seconds):
        return TimeConverter(seconds=seconds)

if __name__ == '__main__':
    converter = TimeConverter(hours=2, minutes=30, seconds=15)
    print(converter.to_seconds())
    print(converter.to_hours())
    print(converter.to_minutes())
    print(converter.to_dhms())
    second_converter = TimeConverter.from_seconds(7265)
    print(second_converter.to_dhms())
    minute_converter = TimeConverter.from_minutes(150)
    print(minute_converter.to_hours())
    hour_converter = TimeConverter.from_hours(0.5)
    print(hour_converter.to_seconds())