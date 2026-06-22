import datetime

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.target_date = datetime.date(year, month, day)

    def get_day_name(self):
        return self.target_date.strftime("%A")

    def get_iso_tuple(self):
        return self.target_date.isocalendar()

if __name__ == '__main__':
    analyzer = DateAnalyzer(2024, 2, 29)
    print(analyzer.get_day_name())
    print(analyzer.get_iso_tuple())