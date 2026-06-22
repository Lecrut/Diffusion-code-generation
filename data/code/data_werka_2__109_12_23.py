import datetime
import calendar

class MonthProgressCalculator:
    def __init__(self, year: int, month: int):
        if not (1 <= month <= 12):
            raise ValueError(f"Invalid month: {month}")
        if year < 1:
            raise ValueError(f"Invalid year: {year}")
        self.year = year
        self.month = month

    def _get_days_in_month(self) -> int:
        return calendar.monthrange(self.year, self.month)[1]

    def _get_current_date(self) -> datetime.date:
        return datetime.date.today()

    def get_total_days(self) -> int:
        return self._get_days_in_month()

    def get_days_passed(self) -> int:
        total_days = self._get_days_in_month()
        today = self._get_current_date()
        first_day = datetime.date(self.year, self.month, 1)
        last_day = datetime.date(self.year, self.month, total_days)

        if today < first_day:
            return 0
        if today > last_day:
            return total_days
        
        return today.day

    def get_days_remaining(self) -> int:
        total_days = self._get_days_in_month()
        days_passed = self.get_days_passed()
        return total_days - days_passed

    def get_percentage_completed(self) -> float:
        total_days = self._get_days_in_month()
        if total_days == 0:
            return 0.0
        days_passed = self.get_days_passed()
        return (days_passed / total_days) * 100

    def get_progress_status(self) -> dict:
        total_days = self.get_total_days()
        days_passed = self.get_days_passed()
        days_remaining = self.get_days_remaining()
        percentage = self.get_percentage_completed()
        
        return {
            "year": self.year,
            "month": self.month,
            "total_days": total_days,
            "days_passed": days_passed,
            "days_remaining": days_remaining,
            "percentage_completed": percentage
        }

if __name__ == '__main__':
    calculator = MonthProgressCalculator(2023, 10)
    status = calculator.get_progress_status()
    print(status)
    print(calculator.get_percentage_completed())
    print(calculator.get_days_remaining())