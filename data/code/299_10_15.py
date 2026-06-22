from datetime import date

class DateUtils:
    @staticmethod
    def is_weekend(year, month, day):
        return date(year, month, day).weekday() >= 5

if __name__ == '__main__':
    print(DateUtils.is_weekend(2023, 10, 7))
    print(DateUtils.is_weekend(2023, 10, 8))