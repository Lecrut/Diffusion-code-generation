from datetime import datetime

class DateCalculator:
    def calculate_difference(self, date1_str, date2_str):
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        return abs(date2 - date1)

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.calculate_difference('2023-01-01', '2023-01-15')
    print(result)