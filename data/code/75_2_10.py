from datetime import datetime

class DateCalculator:
    def calculate_difference(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    result1 = calculator.calculate_difference("2023-01-01", "2023-01-10")
    result2 = calculator.calculate_difference("2023-12-31", "2024-01-01")
    print(result1)
    print(result2)