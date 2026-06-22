from datetime import datetime, timedelta

SECOND_IN_NANOSECONDS = 1_000_000_000
MINUTE_IN_NANOSECONDS = 60 * SECOND_IN_NANOSECONDS
HOUR_IN_NANOSECONDS = 60 * MINUTE_IN_NANOSECONDS
DAY_IN_NANOSECONDS = 24 * HOUR_IN_NANOSECONDS
WEEK_IN_NANOSECONDS = 7 * DAY_IN_NANOSECONDS

class TimeDifferenceCalculator:
    def __init__(self, start_time: datetime, end_time: datetime):
        self.start_time = start_time
        self.end_time = end_time

    def _get_absolute_delta_nanoseconds(self) -> int:
        delta = self.end_time - self.start_time
        total_seconds = abs(delta.total_seconds())
        return int(total_seconds * SECOND_IN_NANOSECONDS)

    def calculate_seconds(self) -> float:
        return self._get_absolute_delta_nanoseconds() / SECOND_IN_NANOSECONDS

    def calculate_minutes(self) -> float:
        return self._get_absolute_delta_nanoseconds() / MINUTE_IN_NANOSECONDS

    def calculate_hours(self) -> float:
        return self._get_absolute_delta_nanoseconds() / HOUR_IN_NANOSECONDS

    def calculate_days(self) -> float:
        return self._get_absolute_delta_nanoseconds() / DAY_IN_NANOSECONDS

    def calculate_weeks(self) -> float:
        return self._get_absolute_delta_nanoseconds() / WEEK_IN_NANOSECONDS

    def calculate_structured(self) -> dict:
        nanoseconds = self._get_absolute_delta_nanoseconds()
        days = nanoseconds // DAY_IN_NANOSECONDS
        remainder = nanoseconds % DAY_IN_NANOSECONDS
        hours = remainder // HOUR_IN_NANOSECONDS
        remainder = remainder % HOUR_IN_NANOSECONDS
        minutes = remainder // MINUTE_IN_NANOSECONDS
        remainder = remainder % MINUTE_IN_NANOSECONDS
        seconds = remainder // SECOND_IN_NANOSECONDS
        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }

    def calculate(self, unit: str = 'structured') -> object:
        if unit == 'seconds':
            return self.calculate_seconds()
        if unit == 'minutes':
            return self.calculate_minutes()
        if unit == 'hours':
            return self.calculate_hours()
        if unit == 'days':
            return self.calculate_days()
        if unit == 'weeks':
            return self.calculate_weeks()
        if unit == 'structured':
            return self.calculate_structured()
        raise ValueError(f"Unknown unit: {unit}")

def main():
    dt1 = datetime(2023, 1, 1, 10, 0, 0)
    dt2 = datetime(2023, 1, 2, 12, 30, 45)
    
    calculator = TimeDifferenceCalculator(dt1, dt2)
    
    print(calculator.calculate('seconds'))
    print(calculator.calculate('minutes'))
    print(calculator.calculate('hours'))
    print(calculator.calculate('days'))
    print(calculator.calculate('weeks'))
    print(calculator.calculate('structured'))

if __name__ == '__main__':
    main()