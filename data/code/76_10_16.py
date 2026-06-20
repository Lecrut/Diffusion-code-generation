from datetime import datetime

class DateCalculator:
    def get_difference(self, date1_str, date2_str):
        try:
            date1 = datetime.strptime(date1_str, '%Y-%m-%d')
            date2 = datetime.strptime(date2_str, '%Y-%m-%d')
            diff = abs(date1 - date2).days
            return diff
        except (TypeError, ValueError):
            return -1

if __name__ == '__main__':
    calculator = DateCalculator()
    result1 = calculator.get_difference("2023-01-01", "2023-01-10")
    print(result1)
    result2 = calculator.get_difference("2024-12-31", "2024-01-01")
    print(result2)