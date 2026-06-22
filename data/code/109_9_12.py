from datetime import date

class MonthCalculator:
    START_DAY = 1

    @staticmethod
    def get_last_day(year, month):
        if month == 12:
            return date(year + 1, 1, MonthCalculator.START_DAY)
        return date(year, month + MonthCalculator.START_DAY, MonthCalculator.START_DAY)

    @staticmethod
    def remaining_days(year, month, current_day):
        first_of_current = date(year, month, MonthCalculator.START_DAY)
        last_of_current = MonthCalculator.get_last_day(year, month)
        total_days_in_month = (last_of_current - first_of_current).days + MonthCalculator.START_DAY
        remaining = total_days_in_month - current_day
        if remaining < 0:
            raise ValueError("Current day is not in the specified month")
        return remaining

if __name__ == '__main__':
    result = MonthCalculator.remaining_days(2023, 10, 15)
    print(result)