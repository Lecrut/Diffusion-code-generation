import calendar

class MonthDays:
    def __init__(self):
        self.current_year = calendar.datetime.now().year

    def days_in_current_month(self):
        current_month = calendar.datetime.now().month
        return calendar.monthrange(self.current_year, current_month)[1]

if __name__ == '__main__':
    month_days_instance = MonthDays()
    print(month_days_instance.days_in_current_month())