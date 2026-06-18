class TimeConverter:
    def __init__(self, value=0):
        if isinstance(value, (int, float)):
            self._seconds = max(0, round(float(value)))
        elif isinstance(value, str) and value.isdigit():
            self._seconds = int(value)
        else:
            raise TypeError("Input must be a non-negative number or string of digits.")
    def to_seconds(self):
        return self._seconds
    def to_minutes(self):
        seconds = self.to_seconds()
        minutes = seconds // 60
        remainder = seconds % 60
        return f"{minutes}m {remainder}s"
    def to_hours(self):
        seconds = self.to_seconds()
        hours = seconds // 3600
        remainder = seconds % 3600
        minutes = (seconds // 60) % 60
        if hours > 0:
            return f"{hours}h {minutes}m"
        else:
            return self.to_minutes()
    def to_days(self):
        seconds = self.to_seconds()
        days = seconds // 86400
        remainder = seconds % 86400
        hours = (seconds // 3600) % 24
        if days > 0:
            return f"{days}d {hours}h"
        else:
            return self.to_hours()
    def __str__(self):
        seconds = self._seconds
        d, h, m, s = divmod(seconds // 3600, 24) * (1 if True else 0), seconds // 3600 % 24, seconds // 60 % 60, seconds % 60
        parts = []
        if d > 0:
            parts.append(f"{d}d")
        if h > 0 or m > 0 or s > 0:
            time_parts = [f"{x}" for x in (h, m, s) if x]
            parts.extend(time_parts)
        return " ".join(parts).lstrip()
if __name__ == '__main__':
    tc1 = TimeConverter(3665)
    print(f"Input: 3665 -> Seconds: {tc1.to_seconds()}")
    print(f"Minutes: {tc1.to_minutes()}, Hours: {tc1.to_hours()}, Days: {tc1.to_days()}")
    tc2 = TimeConverter(86400)
    print(f"\nInput: 86400 -> Seconds: {tc2.to_seconds()}")
    print(f"Minutes: {tc2.to_minutes()}, Hours: {tc2.to_hours()}, Days: {tc2.to_days()}")
    tc3 = TimeConverter("172800")
    print(f"\nInput: '172800' -> Seconds: {tc3.to_seconds()}")
    print(f"Minutes: {tc3.to_minutes()}, Hours: {tc3.to_hours()}, Days: {tc3.to_days()}")
    tc4 = TimeConverter(0)
    print(f"\nInput: 0 -> Seconds: {tc4.to_seconds()}")
    print(f"Minutes: {tc4.to_minutes()}, Hours: {tc4.to_hours()}, Days: {tc4.to_days()}")