from datetime import datetime

class YearDifferenceCalculator:
    def calculate_difference(self, date_str1, date_str2):
        year1 = int(date_str1.split('-')[0])
        year2 = int(date_str2.split('-')[0])
        return abs(year1 - year2)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    difference1 = calculator.calculate_difference("2000-01-01", "1995-01-01")
    difference2 = calculator.calculate_difference("2020-01-01", "2023-01-01")
    print(difference1)
    print(difference2)