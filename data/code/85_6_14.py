class DateDifferenceCalculator:
    DAYS_PER_WEEK = 7

    @staticmethod
    def calculate_week_difference(date1, date2):
        diff = abs((date1 - date2).days)
        return (diff + DateDifferenceCalculator.DAYS_PER_WEEK - 1) // DateDifferenceCalculator.DAYS_PER_WEEK

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    print(calculator.calculate_week_difference(date(2023, 1, 1), date(2023, 1, 8)))