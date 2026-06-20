from datetime import datetime

class DateCalculator:
    DATE_FORMAT = "%Y-%m-%d"

    def calculate_difference(self, date1_str, date2_str):
        date1 = datetime.strptime(date1_str, self.DATE_FORMAT).date()
        date2 = datetime.strptime(date2_str, self.DATE_FORMAT).date()
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = "2023-01-01"
    date_b = "2023-01-15"
    difference = calculator.calculate_difference(date_a, date_b)
    print(difference)