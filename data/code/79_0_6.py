import datetime

class DateCalculator:
    def __init__(self, start_date_str):
        self.start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()

    def calculate_next_month(self):
        year = self.start_date.year
        month = self.start_date.month
        day = self.start_date.day
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        try:
            return datetime.date(next_year, next_month, day)
        except ValueError:
            if month == 2 and day > 28:
                return datetime.date(next_year, next_month, 28)

if __name__ == '__main__':
    calculator = DateCalculator("2023-12-31")
    next_date = calculator.calculate_next_month()
    print(next_date.strftime("%Y-%m-%d"))