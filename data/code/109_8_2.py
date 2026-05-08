class DateUtility:
    def days_left_in_month(self, year, month):
        import calendar
        import datetime
        today = datetime.date.today()
        first_day_of_next_month = today.replace(day=1) + datetime.timedelta(days=32)
        next_month = first_day_of_next_month.replace(day=1)
        days_in_current_month = (next_month - today).days
        days_in_month = calendar.monthrange(year, month)[1]
        return days_in_month - today.day
if __name__ == '__main__':
    utility = DateUtility()
    year = 2023
    month = 10
    days_left = utility.days_left_in_month(year, month)
    print(days_left)