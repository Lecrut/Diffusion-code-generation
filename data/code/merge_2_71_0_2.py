class TimeConverter:
    def __init__(self, seconds: int = 0):
        if not isinstance(seconds, int) or seconds < 0:
            raise TypeError("Seconds must be a non-negative integer.")
        self._seconds = seconds
    @property
    def total_seconds(self) -> float:
        return float(self._seconds)
    def to_minutes(self) -> int:
        if not isinstance(self.total_seconds, (int, float)):
            raise TypeError("Cannot convert invalid time unit.")
        minutes = self.total_seconds // 60
        remainder = self.total_seconds % 60
        return int(minutes + remainder / 60.0)
    def to_hours(self) -> float:
        hours = self.to_minutes() / 60.0
        return round(hours, 2)
    def to_days(self) -> float:
        days = self.to_hours() / 24.0
        return round(days, 2)
if __name__ == '__main__':
    tc1 = TimeConverter(3665)
    print(f"Total Seconds: {tc1.total_seconds}")
    print(f"To Minutes: {tc1.to_minutes()}")
    print(f"To Hours: {tc1.to_hours()}")
    print(f"To Days: {tc1.to_days()}")
    tc2 = TimeConverter(86400)
    print(f"Total Seconds (Day): {tc2.total_seconds}")
    print(f"To Minutes: {tc2.to_minutes()}")
    print(f"To Hours: {tc2.to_hours()}")
    print(f"To Days: {tc2.to_days()}")
    tc3 = TimeConverter(0)
    print(f"Total Seconds (Zero): {tc3.total_seconds}")
    print(f"To Minutes: {tc3.to_minutes()}")
    print(f"To Hours: {tc3.to_hours()}")
    print(f"To Days: {tc3.to_days()}")