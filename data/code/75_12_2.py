from datetime import datetime
from datetime import timedelta
class DateCalculator:
    def calculate_difference(self, date1_str, date2_str):
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        return date2 - date1
if __name__ == '__main__':
    calculator = DateCalculator()
    date1 = "2023-01-01"
    date2 = "2023-01-10"
    difference = calculator.calculate_difference(date1, date2)
    print(difference)