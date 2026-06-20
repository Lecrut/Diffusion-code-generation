from datetime import datetime

class DateCalculator:
    def get_difference(self, date1_str, date2_str):
        try:
            date1 = datetime.strptime(date1_str, '%Y-%m-%d')
            date2 = datetime.strptime(date2_str, '%Y-%m-%d')
            diff = abs((date2 - date1).days)
            return diff
        except ValueError:
            return -1

if __name__ == '__main__':
    calculator = DateCalculator()
    date1_str = "2023-04-01"
    date2_str = "2023-05-15"
    result = calculator.get_difference(date1_str, date2_str)
    print(result)