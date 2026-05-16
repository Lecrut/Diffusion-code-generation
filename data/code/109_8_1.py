import datetime
class DateUtility:
    def days_left_in_month(self, year, month):
        today = datetime.date(year, month, 1)
        first_day_of_next_month = today.replace(day=28) + datetime.timedelta(days=4)
        if month == 12:
            next_month = today.replace(year=year + 1, month=1, day=1)
        else:
            next_month = today.replace(month=month + 1, day=1)
        days_in_current_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
        current_month_days = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
        if month == 12:
            next_month_start = datetime.date(year + 1, 1, 1)
        else:
            next_month_start = datetime.date(year, month + 1, 1)
        days_in_month = (next_month_start - datetime.date(year, month, 1)).days
        return days_in_month - 1
if __name__ == '__main__':
    utility = DateUtility()
    year = 2023
    month = 10
    days_left = utility.days_left_in_month(year, month)
    print(days_left)