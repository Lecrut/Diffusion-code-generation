import datetime

class DateDifferenceCalculator:
    WEEKS_PER_DAY = 7

    @staticmethod
    def calculate_week_difference(date1: datetime.date, date2: datetime.date) -> int:
        difference = abs(date2 - date1)
        return difference.days // DateDifferenceCalculator.WEEKS_PER_DAY
if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 8)
    print(calculator.calculate_week_difference(date1, date2))
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 7)
    print(calculator.calculate_week_difference(date1, date2))
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 1)
    print(calculator.calculate_week_difference(date1, date2))