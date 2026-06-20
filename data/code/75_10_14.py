import datetime

class DateCalculator:
    DATE_FORMAT = "%Y-%m-%d"

    def calculate_difference(self, date1_str: str, date2_str: str) -> datetime.timedelta:
        date1 = datetime.datetime.strptime(date1_str, self.DATE_FORMAT)
        date2 = datetime.datetime.strptime(date2_str, self.DATE_FORMAT)
        return abs(date2 - date1)

if __name__ == '__main__':
    calculator = DateCalculator()
    difference = calculator.calculate_difference('2023-03-01', '2024-03-01')
    print(difference)