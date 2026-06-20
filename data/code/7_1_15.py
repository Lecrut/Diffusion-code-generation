class TimeConverter:
    def __init__(self, total_seconds=0):
        self.total_seconds = int(total_seconds)
        if self.total_seconds < 0:
            self.total_seconds = 0

    def to_hours(self):
        return self.total_seconds // 3600

    def to_minutes(self):
        return self.total_seconds // 60

    def to_seconds(self):
        return self.total_seconds % 60

    def to_hours_with_remainder(self):
        h = self.total_seconds // 3600
        remainder = self.total_seconds % 3600
        m = remainder // 60
        s = remainder % 60
        return h, m, s

    @staticmethod
    def from_hours(hours):
        return int(hours * 3600)

    @staticmethod
    def from_minutes(minutes):
        return int(minutes * 60)

    @staticmethod
    def from_seconds(seconds):
        return int(seconds)

if __name__ == '__main__':
    converter = TimeConverter(3661)
    result = converter.to_hours_with_remainder()
    print(result)