from datetime import datetime

class DateCalculator:
    def calculate_difference(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = "2023-04-01"
    date_b = "2023-05-01"
    difference = calculator.calculate_difference(date_a, date_b)
    print(difference)