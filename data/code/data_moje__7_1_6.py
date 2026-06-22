class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.total_seconds = int(total_seconds)

    def get_hours(self):
        return self.total_seconds // 3600

    def get_minutes(self):
        return (self.total_seconds % 3600) // 60

    def get_seconds(self):
        return self.total_seconds % 60

    def to_total_minutes(self):
        return self.total_seconds / 60

    def to_total_hours(self):
        return self.total_seconds / 3600

    def to_hms_string(self):
        h = self.get_hours()
        m = self.get_minutes()
        s = self.get_seconds()
        return f"{h:02d}:{m:02d}:{s:02d}"

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        return cls(hours, minutes, seconds)

    @classmethod
    def from_minutes(cls, total_minutes):
        total_seconds = int(total_minutes * 60)
        return cls.from_seconds(total_seconds)

    @classmethod
    def from_hours(cls, total_hours):
        total_seconds = int(total_hours * 3600)
        return cls.from_seconds(total_seconds)

if __name__ == '__main__':
    converter = TimeConverter(hours=2, minutes=45, seconds=30)
    print(converter.to_hms_string())
    print(converter.to_total_minutes())
    print(converter.get_seconds())
    new_converter = TimeConverter.from_seconds(5000)
    print(new_converter.to_hms_string())