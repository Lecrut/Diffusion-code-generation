from datetime import date, timedelta

class DateCalculator:
    START_DATE = date(2024, 1, 1)
    WEEK_OFFSET = 7

    @staticmethod
    def _add_days(d: date, days: int) -> date:
        return d + timedelta(days=days)

    @classmethod
    def find_next_weekly_marker(cls) -> date:
        return cls._add_days(cls.START_DATE, cls.WEEK_OFFSET)

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.find_next_weekly_marker()
    print(result)