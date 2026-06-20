from datetime import date, timedelta

class DateShifter:

    def __init__(self, start_date):
        self.start_date = start_date

    def add_months(self, months_to_add):
        year = self.start_date.year
        month = self.start_date.month
        total_months = month + months_to_add
        new_year = year + (total_months - 1) // 12
        new_month = (total_months - 1) % 12 + 1
        while True:
            try:
                return date(new_year, new_month, self.start_date.day)
            except ValueError:
                new_day = min(self.start_date.day, calendar.monthrange(new_year, new_month)[1])
                return date(new_year, new_month, new_day)
if __name__ == '__main__':
    shifter = DateShifter(date(2023, 9, 10))
    next_monday = shifter.add_months(1)
    while next_monday.weekday() != 0:
        next_monday += timedelta(days=1)
    print(next_monday)