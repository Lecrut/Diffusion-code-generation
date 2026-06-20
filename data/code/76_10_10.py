from datetime import datetime

class DateCalculator:
    def get_difference(self, date1_str, date2_str):
        try:
            date1 = datetime.strptime(date1_str, '%Y-%m-%d')
            date2 = datetime.strptime(date2_str, '%Y-%m-%d')
            diff = abs((date2 - date1).days)
            return diff
        except (TypeError, ValueError):
            return None

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.get_difference("2023-01-01", "2023-01-10")
    print(result)