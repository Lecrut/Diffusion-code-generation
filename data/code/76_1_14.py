import datetime

class DateCalculator:
    def days_between(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(date1_str, date_format)
        date2 = datetime.datetime.strptime(date2_str, date_format)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.days_between("2023-01-01", "2023-01-15"))
    print(calculator.days_between("2023-02-01", "2023-03-15"))