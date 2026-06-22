import datetime

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_day_name(self):
        return self.date_obj.strftime("%A")

    def get_weekday_index(self):
        return self.date_obj.weekday()

    def is_leap_year(self):
        return self.date_obj.year % 4 == 0 and (self.date_obj.year % 100 != 0 or self.date_obj.year % 400 == 0)

if __name__ == '__main__':
    analyzer = DateAnalyzer(2024, 2, 29)
    print(analyzer.get_day_name())
    print(analyzer.get_weekday_index())
    print(analyzer.is_leap_year())