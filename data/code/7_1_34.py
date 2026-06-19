class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def to_hours(self):
        return self.total_seconds / 3600

    def to_minutes(self):
        return self.total_seconds / 60

    def to_seconds(self):
        return self.total_seconds

if __name__ == '__main__':
    converter = TimeConverter(hours=2, minutes=30, seconds=15)
    print("Total hours:", converter.to_hours())
    print("Total minutes:", converter.to_minutes())
    print("Total seconds:", converter.to_seconds())