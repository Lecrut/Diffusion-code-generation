from datetime import datetime

class TimeDeltaCalculator:
    def calculate_timedelta_in_hours(self, dt1, dt2):
        difference = dt2 - dt1
        hours = difference.total_seconds() / 3600.0
        return hours

if __name__ == '__main__':
    calculator = TimeDeltaCalculator()
    datetime1 = datetime(2023, 4, 1, 12, 0, 0)
    datetime2 = datetime(2023, 4, 1, 18, 0, 0)
    result = calculator.calculate_timedelta_in_hours(datetime1, datetime2)
    print(result)