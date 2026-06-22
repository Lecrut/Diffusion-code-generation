import datetime

class MonthCalculator:
    DAYS_IN_MONTHS = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    @staticmethod
    def _is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def get_days_remaining(target_date):
        year = target_date.year
        month = target_date.month
        day = target_date.day

        if month < 1 or month > 12:
            raise ValueError("Invalid month")

        total_days_in_month = MonthCalculator.DAYS_IN_MONTHS[month]
        if month == 2 and MonthCalculator._is_leap_year(year):
            total_days_in_month = 29

        last_day_of_month = total_days_in_month
        remaining_days = last_day_of_month - day
        return remaining_days

if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 15),
        datetime.date(2023, 2, 28),
        datetime.date(2024, 2, 29),
        datetime.date(2023, 12, 31)
    ]
    for d in sample_dates:
        result = MonthCalculator.get_days_remaining(d)
        print(f"Days remaining for {d}: {result}")