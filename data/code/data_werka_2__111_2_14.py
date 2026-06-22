from datetime import date

class DateAnalyzer:
    def __init__(self, year, month, day):
        self._date = date(year, month, day)

    def get_weekday(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[self._date.weekday()]

if __name__ == '__main__':
    analyzer = DateAnalyzer(2024, 2, 29)
    print(analyzer.get_weekday())