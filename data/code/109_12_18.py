class MonthProgressCalculator:
    DAYS_IN_WEEK = 7
    MONTHS_IN_YEAR = 12
    MIN_MONTH = 1
    MAX_MONTH = 12

    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        self._validate()

    def _validate(self):
        if not (self.MIN_MONTH <= self.month <= self.MAX_MONTH):
            raise ValueError("Month must be between 1 and 12")
        if self.year < 1:
            raise ValueError("Year must be positive")

    @staticmethod
    def _get_days_in_month(year: int, month: int) -> int:
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        if month in (4, 6, 9, 11):
            return 30
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            return 28
        return 0

    def calculate(self) -> dict:
        import datetime
        today = datetime.date.today()
        first_day = datetime.date(self.year, self.month, 1)
        last_day = datetime.date(self.year, self.month, self._get_days_in_month(self.year, self.month))

        total_days = last_day.day

        if today < first_day:
            days_passed = 0
            remaining_days = total_days
        elif today > last_day:
            days_passed = total_days
            remaining_days = 0
        else:
            delta = today - first_day
            days_passed = delta.days + 1
            remaining_days = total_days - days_passed

        percentage = (days_passed / total_days) * 100 if total_days > 0 else 0.0

        return {
            "year": self.year,
            "month": self.month,
            "total_days": total_days,
            "days_passed": days_passed,
            "remaining_days": remaining_days,
            "percentage_completed": percentage
        }

if __name__ == '__main__':
    calculator = MonthProgressCalculator(2023, 10)
    result = calculator.calculate()
    print(result)