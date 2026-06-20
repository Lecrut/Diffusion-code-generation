from datetime import datetime

class DateCalculator:
    DATE_FORMAT = "%Y-%m-%d"

    def calculate_difference(self, date1_str, date2_str):
        date1 = datetime.strptime(date1_str, self.DATE_FORMAT)
        date2 = datetime.strptime(date2_str, self.DATE_FORMAT)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.calculate_difference("2023-01-01", "2023-01-15")
    print(result)