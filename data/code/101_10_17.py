import calendar

class DateAnalyzer:
    def __init__(self, year: int, month: int, day: int):
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise ValueError("Arguments must be integers")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if not (1 <= day <= 31):
            raise ValueError("Day must be between 1 and 31")
        try:
            calendar.weekday(year, month, day)
        except ValueError:
            raise ValueError("Invalid date provided")
        self.year = year
        self.month = month
        self.day = day

    def get_weekday_name(self) -> str:
        index = calendar.weekday(self.year, self.month, self.day)
        return calendar.day_name[index]

if __name__ == '__main__':
    analyzer = DateAnalyzer(2023, 12, 25)
    print(analyzer.get_weekday_name())