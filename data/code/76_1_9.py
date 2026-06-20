from datetime import datetime

class DateCalculator:
    def days_between(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        delta = abs((date2 - date1).days)
        return delta

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.days_between("2023-01-01", "2023-01-15")
    print(result)