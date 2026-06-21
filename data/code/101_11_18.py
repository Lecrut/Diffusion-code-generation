import datetime

class DateAnalyzer:
    WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_day_name(self):
        return self.WEEKDAYS[self.date_obj.weekday()]

if __name__ == '__main__':
    analyzer = DateAnalyzer(2023, 10, 10)
    print(analyzer.get_day_name())