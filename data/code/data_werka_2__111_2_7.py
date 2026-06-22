class DateAnalyzer:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.target_date = None

    def compute_date(self):
        import datetime
        self.target_date = datetime.date(self.year, self.month, self.day)
        return self

    def get_full_day_name(self):
        if self.target_date is None:
            raise ValueError("Date not computed")
        return self.target_date.strftime("%A")

    def get_ordinal_weekday(self):
        if self.target_date is None:
            raise ValueError("Date not computed")
        return self.target_date.weekday()

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

if __name__ == '__main__':
    analyzer = DateAnalyzer(2024, 2, 29)
    analyzer.compute_date()
    print(analyzer.get_full_day_name())
    print(analyzer.get_ordinal_weekday())
    print(analyzer.is_leap_year())