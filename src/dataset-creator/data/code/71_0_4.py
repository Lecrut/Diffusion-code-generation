class TimeConverter:
    def __init__(self, value=0):
        self.value = float(value) if isinstance(value, (int, float)) else 0
    @staticmethod
    def validate_input(val):
        try:
            val = float(val)
            return True
        except ValueError:
            raise TypeError("Input must be a numeric value.")
    def to_seconds(self):
        self.validate_input(self.value)
        if isinstance(self.value, int):
            return int(float(self.value))
        else:
            return round(self.value * 1.0)
    def to_minutes(self):
        seconds = self.to_seconds()
        return int(seconds / 60)
    def to_hours(self):
        minutes = self.to_minutes()
        return int(minutes / 60)
    def to_days(self):
        hours = self.to_hours()
        return int(hours / 24)
if __name__ == '__main__':
    tc1 = TimeConverter(3600)
    print(f"Seconds: {tc1.to_seconds()}")
    print(f"Minutes: {tc1.to_minutes()}")
    tc2 = TimeConverter("7.5 hours")
    seconds_val = float(tc2.value * 3600) if isinstance(tc2.value, (int, float)) else None
    sample_tc = TimeConverter(86400)
    print(f"Days: {sample_tc.to_days()}")