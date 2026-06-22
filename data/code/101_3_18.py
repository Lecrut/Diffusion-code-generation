import datetime

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_weekday_name(self):
        return self.date_obj.strftime("%A")

    def get_weekday_number(self):
        return self.date_obj.weekday()

if __name__ == '__main__':
    analyzer = DateAnalyzer(2023, 12, 25)
    print(analyzer.get_weekday_name())
    print(analyzer.get_weekday_number())