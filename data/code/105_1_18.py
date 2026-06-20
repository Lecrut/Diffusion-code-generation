class DateCalculator:
    TARGET_YEAR = 2024

    @staticmethod
    def first_sunday_after_jan_1():
        target_date = date(DateCalculator.TARGET_YEAR, 1, 1)
        while target_date.weekday() != 6:
            target_date += timedelta(days=1)
        return target_date

if __name__ == '__main__':
    result = DateCalculator.first_sunday_after_jan_1()
    print(result)