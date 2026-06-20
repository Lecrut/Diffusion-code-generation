class TimeConverter:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def from_hours(self, h):
        self.hours = h
        self.minutes = h * 60
        self.seconds = h * 3600
        return self

    def from_minutes(self, m):
        self.hours = m / 60.0
        self.minutes = m
        self.seconds = m * 60
        return self

    def from_seconds(self, s):
        self.hours = s / 3600.0
        self.minutes = s / 60.0
        self.seconds = s
        return self

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.minutes

    def get_seconds(self):
        return self.seconds

    def convert_to_hours(self):
        return self.seconds / 3600.0

    def convert_to_minutes(self):
        return self.seconds / 60.0

    def convert_to_seconds(self):
        return self.seconds

if __name__ == '__main__':
    converter = TimeConverter()
    converter.from_minutes(150)
    print(converter.get_hours())
    print(converter.get_minutes())
    print(converter.get_seconds())
    print(converter.convert_to_hours())