import datetime

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_day_name(self):
        return self.date_obj.strftime("%A")

    def get_day_number(self):
        return self.date_obj.weekday()

    def is_weekend(self):
        return self.date_obj.weekday() in (5, 6)

if __name__ == '__main__':
    analyzer = DateAnalyzer(2023, 10, 10)
    print(analyzer.get_day_name())
    print(analyzer.get_day_number())
    print(analyzer.is_weekend())