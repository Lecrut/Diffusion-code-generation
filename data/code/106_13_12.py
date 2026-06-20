import datetime

class YearDifferenceCalculator:
    @staticmethod
    def calculate(timestamp1, timestamp2):
        date1 = datetime.datetime.fromtimestamp(timestamp1)
        date2 = datetime.datetime.fromtimestamp(timestamp2)
        return abs(date1.year - date2.year)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    print(calculator.calculate(1609459200, 1672531200))