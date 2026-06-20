class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def to_minutes(self):
        return self.hours * 60 + self.minutes + self.seconds / 60

    def to_hours(self):
        return self.hours + self.minutes / 60 + self.seconds / 3600

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = int(total_seconds // 3600)
        remainder = total_seconds % 3600
        minutes = int(remainder // 60)
        seconds = remainder % 60
        return cls(hours, minutes, seconds)

    @classmethod
    def from_minutes(cls, total_minutes):
        hours = int(total_minutes // 60)
        remainder = total_minutes % 60
        minutes = int(remainder)
        seconds = (remainder - minutes) * 60
        return cls(hours, minutes, seconds)

    @classmethod
    def from_hours(cls, total_hours):
        hours = int(total_hours)
        remainder = total_hours - hours
        minutes = int(remainder * 60)
        seconds = (remainder * 60 - minutes) * 60
        return cls(hours, minutes, seconds)

    def __repr__(self):
        return f"TimeConverter(hours={self.hours}, minutes={self.minutes}, seconds={self.seconds})"

if __name__ == '__main__':
    converter = TimeConverter(2, 30, 45)
    print(converter.to_seconds())
    print(converter.to_minutes())
    print(converter.to_hours())

    new_converter = TimeConverter.from_seconds(9045)
    print(new_converter)

    another_converter = TimeConverter.from_minutes(150.75)
    print(another_converter)

    final_converter = TimeConverter.from_hours(3.5)
    print(final_converter)