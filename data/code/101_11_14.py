import datetime

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_full_day_name(self):
        return self.date_obj.strftime("%A")

    def get_short_day_name(self):
        return self.date_obj.strftime("%a")

    def get_month_name(self):
        return self.date_obj.strftime("%B")

    def get_day_number(self):
        return self.date_obj.day

if __name__ == '__main__':
    analyzer = DateAnalyzer(2023, 10, 10)
    print(analyzer.get_full_day_name())
    print(analyzer.get_short_day_name())
    print(analyzer.get_month_name())
    print(analyzer.get_day_number())