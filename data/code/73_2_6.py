from datetime import datetime, timedelta

class TimeCalculator:
    def calculate_difference(self, start_time, end_time):
        if not isinstance(start_time, datetime):
            raise TypeError("start_time must be a datetime object")
        if not isinstance(end_time, datetime):
            raise TypeError("end_time must be a datetime object")
        delta = end_time - start_time
        total_seconds = int(delta.total_seconds())
        abs_seconds = abs(total_seconds)
        days = abs_seconds // 86400
        hours = (abs_seconds % 86400) // 3600
        minutes = (abs_seconds % 3600) // 60
        seconds = abs_seconds % 60
        sign = "-" if total_seconds < 0 else ""
        return f"{sign}{days}d {hours:02d}h {minutes:02d}m {seconds:02d}s"

if __name__ == '__main__':
    calculator = TimeCalculator()
    t1 = datetime(2024, 6, 15, 8, 30, 0)
    t2 = datetime(2024, 6, 20, 10, 45, 30)
    result = calculator.calculate_difference(t1, t2)
    print(f"Start: {t1}")
    print(f"End: {t2}")
    print(f"Diff: {result}")