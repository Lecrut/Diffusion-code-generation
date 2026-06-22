class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def to_hours(self):
        return self.total_seconds // 3600

    def to_minutes(self):
        return (self.total_seconds % 3600) // 60

    def to_seconds(self):
        return self.total_seconds % 60

    def add_time(self, hours=0, minutes=0, seconds=0):
        additional_seconds = hours * 3600 + minutes * 60 + seconds
        self.total_seconds += additional_seconds

    def subtract_time(self, hours=0, minutes=0, seconds=0):
        subtracted_seconds = hours * 3600 + minutes * 60 + seconds
        self.total_seconds = max(0, self.total_seconds - subtracted_seconds)

if __name__ == '__main__':
    converter = TimeConverter(hours=2, minutes=45, seconds=30)
    print("Initial time in hours:", converter.to_hours())
    print("Initial time in minutes:", converter.to_minutes())
    print("Initial time in seconds:", converter.to_seconds())

    converter.add_time(minutes=15, seconds=45)
    print("After adding 15 minutes and 45 seconds:")
    print("Time in hours:", converter.to_hours())
    print("Time in minutes:", converter.to_minutes())
    print("Time in seconds:", converter.to_seconds())

    converter.subtract_time(hours=1, seconds=30)
    print("After subtracting 1 hour and 30 seconds:")
    print("Time in hours:", converter.to_hours())
    print("Time in minutes:", converter.to_minutes())
    print("Time in seconds:", converter.to_seconds())