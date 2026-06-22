import calendar

class MonthDays:
    def days_left_in_month(self, month: int, year: int) -> int:
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        return calendar.monthrange(year, month)[1]

if __name__ == '__main__':
    month_days = MonthDays()
    print(month_days.days_left_in_month(1, 2023))
    print(month_days.days_left_in_month(12, 2023))
    print(month_days.days_left_in_month(2, 2024))
    print(month_days.days_left_in_month(7, 2025))