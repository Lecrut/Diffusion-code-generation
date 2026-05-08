import datetime
class DateUtility:
    def days_left_in_month(self, year, month):
        today = datetime.date(year, month, 1)
        first_day_of_next_month = datetime.date(year, month + 1, 1)
        days_in_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
        days_left = datetime.date(year, month, 1) + datetime.timedelta(days=days_in_month) - datetime.date(year, month, 1)
        return (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days - 1
if __name__ == '__main__':
    utility = DateUtility()
    year = 2023
    month = 10
    days_left = utility.days_left_in_month(year, month)
    print(days_left)