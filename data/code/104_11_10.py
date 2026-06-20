import datetime

class DateDifferenceCalculator:

    @staticmethod
    def calculate_difference(date1, date2):
        if not isinstance(date1, datetime.datetime) or not isinstance(date2, datetime.datetime):
            raise ValueError('Both arguments must be instances of datetime.datetime')
        return abs((date2 - date1).days)
if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    d2 = datetime.datetime(2023, 10, 25, 15, 45, 0)
    d3 = datetime.datetime(2024, 1, 1, 0, 0, 0)
    d4 = datetime.datetime(2024, 1, 1, 0, 0, 0)
    calculator = DateDifferenceCalculator()
    print(calculator.calculate_difference(d1, d2))
    print(calculator.calculate_difference(d3, d4))
    print(calculator.calculate_difference(d2, d1))
    print(calculator.calculate_difference(d4, d3))
    print(calculator.calculate_difference(d1, d1))