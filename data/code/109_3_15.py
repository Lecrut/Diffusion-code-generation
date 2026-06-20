from datetime import date

class MonthUtils:
    @staticmethod
    def days_left_in_month():
        today = date.today()
        _, num_days = MonthUtils._get_month_range(today)
        return num_days - today.day
    
    @staticmethod
    def _get_month_range(date):
        return calendar.monthrange(date.year, date.month)

if __name__ == '__main__':
    print(MonthUtils.days_left_in_month())