class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        return total_seconds

    def to_minutes(self):
        total_seconds = self.to_seconds()
        return total_seconds / 60

    def to_hours(self):
        total_seconds = self.to_seconds()
        return total_seconds / 3600

    def normalize(self):
        total_seconds = self.to_seconds()
        self.hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        self.minutes = remaining_seconds // 60
        self.seconds = remaining_seconds % 60
        return self

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

if __name__ == '__main__':
    tc = TimeConverter(hours=2, minutes=45, seconds=30)
    print(f"Total seconds: {tc.to_seconds()}")
    print(f"Total minutes: {tc.to_minutes()}")
    print(f"Total hours: {tc.to_hours()}")
    tc_normalized = TimeConverter(hours=0, minutes=0, seconds=7265)
    tc_normalized.normalize()
    print(f"Normalized time: {tc_normalized}")