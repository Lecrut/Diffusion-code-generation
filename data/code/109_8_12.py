import datetime

class DateUtility:
    @staticmethod
    def days_left_in_month(year, month):
        today = datetime.date(year, month, 1)
        first_day_of_next_month = today.replace(day=28) + datetime.timedelta(days=4)
        next_month = first_day_of_next_month.replace(day=1)
        days_in_current_month = (next_month - today).days
        return days_in_current_month

if __name__ == '__main__':
    utility = DateUtility()
    year = 2023
    month = 10
    days_left = utility.days_left_in_month(year, month)
    print(days_left)