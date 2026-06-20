import datetime

class DateDifferenceCalculator:
    START_DATE = datetime.date(2023, 1, 1)
    END_DATE = datetime.date(2023, 12, 31)

    @staticmethod
    def calculate_days_between(start, end):
        delta = end - start
        return delta.days

if __name__ == '__main__':
    result = DateDifferenceCalculator.calculate_days_between(DateDifferenceCalculator.START_DATE, DateDifferenceCalculator.END_DATE)
    print(result)