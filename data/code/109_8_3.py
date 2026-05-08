import datetime
class DateUtility:
    def days_left_in_month(self, year, month):
        today = datetime.date(year, month, 1)
        first_day_of_next_month = datetime.date(year, month + 1, 1)
        days_in_current_month = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
        return (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
if __name__ == '__main__':
    utility = DateUtility()
    year = 2023
    month = 10
    days_left = utility.days_left_in_month(year, month)
    print(days_left)