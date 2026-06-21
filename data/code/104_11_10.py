from datetime import datetime

class DateTimeCalculator:
    MAX_DAYS = 999999999
    MIN_DAYS = -999999999

    @staticmethod
    def validate_naive(dt: datetime) -> None:
        if dt.tzinfo is not None:
            raise ValueError("Timezone-aware datetimes are not supported.")

    @classmethod
    def calculate_days_difference(cls, dt1: datetime, dt2: datetime) -> int:
        cls.validate_naive(dt1)
        cls.validate_naive(dt2)
        delta = dt2 - dt1
        days = delta.days
        if days > cls.MAX_DAYS or days < cls.MIN_DAYS:
            raise ValueError("Resulting day difference is out of range.")
        return days

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 0, 0, 0)
    end = datetime(2023, 1, 15, 0, 0, 0)
    calc = DateTimeCalculator()
    result = calc.calculate_days_difference(start, end)
    print(result)