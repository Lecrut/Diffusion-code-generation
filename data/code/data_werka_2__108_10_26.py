class DateCalculator:
    JANUARY = 1
    TARGET_DAY = 1
    TARGET_YEAR = 2024

    @staticmethod
    def get_january_1_day(year):
        import datetime
        date_obj = datetime.date(year, DateCalculator.JANUARY, DateCalculator.TARGET_DAY)
        return date_obj.strftime("%A")

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.get_january_1_day(DateCalculator.TARGET_YEAR)
    print(result)