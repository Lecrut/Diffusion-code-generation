import datetime

class Date:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def add_year_and_day(self):
        new_date = self.date.replace(year=self.date.year + 1)
        if new_date.month == 2 and self.is_leap_year(new_date.year):
            new_date += datetime.timedelta(days=1)
        return new_date

if __name__ == '__main__':
    date_obj = Date(2020, 12, 31)
    result = date_obj.add_year_and_day()
    print(result)