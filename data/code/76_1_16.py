import datetime

class DateCalculator:
    def days_between(self, date1_str: str, date2_str: str) -> int:
        date_format = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(date1_str, date_format)
        date2 = datetime.datetime.strptime(date2_str, date_format)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = "2023-02-01"
    date_b = "2023-02-28"
    result = calculator.days_between(date_a, date_b)
    print(result)