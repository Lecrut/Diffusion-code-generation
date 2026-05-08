import datetime
class DateUtility:
    def days_left_in_month(self, year, month):
        today = datetime.date(year, month, 1)
        first_day_of_next_month = datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1)
        delta = first_day_of_next_month - today
        return delta.days - 1
if __name__ == '__main__':
    utility = DateUtility()
    year = 2023
    month = 10
    days_left = utility.days_left_in_month(year, month)
    print(days_left)