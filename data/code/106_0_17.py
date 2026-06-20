from datetime import datetime

class DateDifferenceCalculator:
    def __init__(self, date_str1: str, date_str2: str):
        self.date_format = "%Y-%m-%d"
        self.date1 = datetime.strptime(date_str1, self.date_format)
        self.date2 = datetime.strptime(date_str2, self.date_format)

    def calculate_difference(self) -> int:
        return abs((self.date2 - self.date1).days) // 365

if __name__ == '__main__':
    calculator = DateDifferenceCalculator("1990-05-15", "2023-04-10")
    print(calculator.calculate_difference())