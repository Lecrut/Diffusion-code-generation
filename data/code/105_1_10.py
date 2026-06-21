import datetime

class DateCalculator:
    BASE_DATE = datetime.date(2024, 1, 1)
    TARGET_WEEKDAY = 6

    @staticmethod
    def calculate_first_sunday_after_base():
        current = DateCalculator.BASE_DATE
        while current.weekday() != DateCalculator.TARGET_WEEKDAY:
            current = current + datetime.timedelta(days=1)
        return current

if __name__ == '__main__':
    result = DateCalculator.calculate_first_sunday_after_base()
    print(result)