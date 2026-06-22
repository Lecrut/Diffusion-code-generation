import datetime
import calendar

DAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def get_name(self):
        weekday = self.date.weekday()
        return DAY_MAP[weekday]

if __name__ == '__main__':
    analyzer = DateAnalyzer(2024, 2, 29)
    print(analyzer.get_name())