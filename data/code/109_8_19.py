import datetime

class DateUtility:
    def days_left_in_month(self, year, month):
        today = datetime.date(year, month, 1)
        first_day_of_next_month = today.replace(day=28) + datetime.timedelta(days=4)
        if month == 12:
            next_month = today.replace(year=year + 1, month=1, day=1)
        else:
            next_month = today.replace(month=month + 1, day=1)
        days_in_current_month = (next_month - today).days
        return days_in_current_month

if __name__ == '__main__':
    utility = DateUtility()
    year = 2023
    month = 5
    days_left = utility.days_left_in_month(year, month)
    print(days_left)