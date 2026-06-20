from datetime import datetime

class YearDifferenceCalculator:
    def calculate_year_difference(self, date1: datetime, date2: datetime) -> int:
        return abs((date2.year - date1.year))

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    date1 = datetime(2000, 5, 15)
    date2 = datetime(2023, 8, 20)
    difference = calculator.calculate_year_difference(date1, date2)
    print(difference)