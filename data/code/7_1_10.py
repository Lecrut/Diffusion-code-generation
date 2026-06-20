class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.hours = total_seconds // 3600
        remainder = total_seconds % 3600
        self.minutes = remainder // 60
        self.seconds = remainder % 60

    def convert_to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def convert_to_minutes(self):
        total_seconds = self.convert_to_seconds()
        return total_seconds / 60.0

    def convert_to_hours(self):
        total_seconds = self.convert_to_seconds()
        return total_seconds / 3600.0

    def add(self, other):
        total_seconds = self.convert_to_seconds() + other.convert_to_seconds()
        new_hours = total_seconds // 3600
        remainder = total_seconds % 3600
        new_minutes = remainder // 60
        new_seconds = remainder % 60
        return TimeConverter(new_hours, new_minutes, new_seconds)

    def subtract(self, other):
        total_seconds = self.convert_to_seconds() - other.convert_to_seconds()
        if total_seconds < 0:
            total_seconds = 0
        new_hours = total_seconds // 3600
        remainder = total_seconds % 3600
        new_minutes = remainder // 60
        new_seconds = remainder % 60
        return TimeConverter(new_hours, new_minutes, new_seconds)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

if __name__ == '__main__':
    tc1 = TimeConverter(2, 30, 45)
    tc2 = TimeConverter(1, 15, 30)
    
    print(f"Time 1 in seconds: {tc1.convert_to_seconds()}")
    print(f"Time 1 in minutes: {tc1.convert_to_minutes()}")
    print(f"Time 1 in hours: {tc1.convert_to_hours()}")
    
    added = tc1.add(tc2)
    print(f"Time 1 + Time 2: {added}")
    
    subtracted = tc1.subtract(tc2)
    print(f"Time 1 - Time 2: {subtracted}")