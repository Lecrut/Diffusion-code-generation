import datetime

class MonthDaysCalculator:
    @staticmethod
    def get_days_in_month(year, month):
        return calendar.monthrange(year, month)[1]

    @staticmethod
    def calculate_remaining_days(current_date):
        days_in_month = MonthDaysCalculator.get_days_in_month(current_date.year, current_date.month)
        if current_date.day == 1:
            return days_in_month
        else:
            return days_in_month - (current_date.day - 1)

if __name__ == '__main__':
    target_date = datetime.date(2023, 10, 15)
    remaining_days = MonthDaysCalculator.calculate_remaining_days(target_date)
    print(remaining_days)