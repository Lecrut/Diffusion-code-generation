import datetime

class DateDifferenceCalculator:
    START_DATE = datetime.date(2023, 1, 1)
    END_DATE = datetime.date(2023, 12, 31)

    @staticmethod
    def calculate_days_difference(start_date=START_DATE, end_date=END_DATE):
        delta = end_date - start_date
        return delta.days

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    days_between = calculator.calculate_days_difference()
    print(f"Number of days between {DateDifferenceCalculator.START_DATE} and {DateDifferenceCalculator.END_DATE}: {days_between}")