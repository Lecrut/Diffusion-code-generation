from datetime import date, timedelta

class DateCalculator:
    def __init__(self, start_date):
        self.start_date = start_date

    def get_weekday_index(self):
        return self.start_date.weekday()

    def calculate_days_to_saturday(self):
        current_index = self.get_weekday_index()
        target_index = 5
        difference = target_index - current_index
        if difference <= 0:
            difference += 7
        return difference

    def find_nearest_saturday(self):
        days_to_add = self.calculate_days_to_saturday()
        return self.start_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    calc = DateCalculator(date(2023, 11, 1))
    print(calc.find_nearest_saturday())
    print(calc.get_weekday_index())