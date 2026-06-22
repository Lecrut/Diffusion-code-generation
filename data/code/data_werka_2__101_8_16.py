import calendar

class DateWeekdayCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def calculate(self):
        index = calendar.weekday(self.year, self.month, self.day)
        return calendar.day_name[index]

if __name__ == '__main__':
    calc1 = DateWeekdayCalculator(2023, 10, 25)
    print(calc1.calculate())
    calc2 = DateWeekdayCalculator(2024, 2, 29)
    print(calc2.calculate())