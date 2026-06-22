import datetime

class DateAnalyzer:
    _DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self, year, month, day):
        self._date = datetime.date(year, month, day)

    @staticmethod
    def get_day_name(year, month, day):
        d = datetime.date(year, month, day)
        return DateAnalyzer._DAYS[d.weekday()]

    def get_weekday_name(self):
        return DateAnalyzer._DAYS[self._date.weekday()]

if __name__ == '__main__':
    analyzer = DateAnalyzer(2025, 3, 15)
    print(analyzer.get_weekday_name())