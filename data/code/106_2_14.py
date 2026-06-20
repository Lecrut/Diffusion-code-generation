from datetime import datetime

class YearDifferenceCalculator:
    def calculate_year_difference(self, date1: datetime, date2: datetime) -> int:
        return abs(date2.year - date1.year)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    date1 = datetime(1980, 6, 30)
    date2 = datetime(2023, 5, 15)
    difference_1 = calculator.calculate_year_difference(date1, date2)
    print(difference_1)

    date3 = datetime(2010, 12, 25)
    date4 = datetime(2015, 1, 1)
    difference_2 = calculator.calculate_year_difference(date3, date4)
    print(difference_2)