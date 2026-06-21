import calendar

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_weekday_name(self):
        index = calendar.weekday(self.year, self.month, self.day)
        return calendar.day_name[index]

    def get_weekday_index(self):
        return calendar.weekday(self.year, self.month, self.day)

    def is_leap_year(self):
        return calendar.isleap(self.year)

if __name__ == '__main__':
    analyzer = DateAnalyzer(2023, 12, 25)
    print(analyzer.get_weekday_name())
    print(analyzer.get_weekday_index())
    print(analyzer.is_leap_year())