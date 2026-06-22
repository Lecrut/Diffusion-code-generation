import datetime

class DateCalculator:
    def __init__(self, year, month, day):
        self.base_date = datetime.date(year, month, day)

    def find_first_sunday(self):
        current = self.base_date
        while current.weekday() != 6:
            current = current + datetime.timedelta(days=1)
        return current

    def get_formatted_date(self):
        return self.base_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    calc = DateCalculator(2024, 1, 1)
    sunday = calc.find_first_sunday()
    print(sunday)
    print(calc.get_formatted_date())