import datetime

class YearCalculator:
    def __init__(self):
        self.year = 2023

    def calculate_total_seconds(self):
        start_date = datetime.date(self.year, 1, 1)
        end_date = datetime.date(self.year, 12, 31)
        delta = end_date - start_date
        return delta.total_seconds()

if __name__ == '__main__':
    calculator = YearCalculator()
    total_seconds = calculator.calculate_total_seconds()
    print(total_seconds)