import datetime

class DayOfWeekCalculator:
    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_name(self):
        return self.date_obj.strftime("%A")

    def get_abbreviated(self):
        return self.date_obj.strftime("%a")

    def get_iso_weekday(self):
        return self.date_obj.isoweekday()

if __name__ == '__main__':
    calculator = DayOfWeekCalculator(2023, 10, 10)
    print(calculator.get_name())
    print(calculator.get_abbreviated())
    print(calculator.get_iso_weekday())