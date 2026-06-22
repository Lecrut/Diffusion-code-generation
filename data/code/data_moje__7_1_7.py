class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = self._normalize_to_seconds()

    def _normalize_to_seconds(self):
        total = self.hours * 3600 + self.minutes * 60 + self.seconds
        return total

    def get_hours(self):
        return self.total_seconds // 3600

    def get_minutes(self):
        return (self.total_seconds // 60) % 60

    def get_seconds(self):
        return self.total_seconds % 60

    def get_total_seconds(self):
        return self.total_seconds

    def to_hms(self):
        return self.get_hours(), self.get_minutes(), self.get_seconds()

    def set_from_seconds(self, total_seconds):
        self.total_seconds = total_seconds
        self.hours = self.total_seconds // 3600
        remaining = self.total_seconds % 3600
        self.minutes = remaining // 60
        self.seconds = remaining % 60
        return self

    def add(self, hours=0, minutes=0, seconds=0):
        self.total_seconds += hours * 3600 + minutes * 60 + seconds
        self.hours = self.total_seconds // 3600
        remaining = self.total_seconds % 3600
        self.minutes = remaining // 60
        self.seconds = remaining % 60
        return self

    def subtract(self, hours=0, minutes=0, seconds=0):
        amount = hours * 3600 + minutes * 60 + seconds
        self.total_seconds -= amount
        self.hours = self.total_seconds // 3600
        remaining = self.total_seconds % 3600
        self.minutes = remaining // 60
        self.seconds = remaining % 60
        return self

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

if __name__ == '__main__':
    tc = TimeConverter(hours=1, minutes=30, seconds=45)
    print(tc.to_hms())
    print(tc.get_total_seconds())
    tc.add(minutes=30)
    print(tc)
    tc.set_from_seconds(9005)
    print(tc)