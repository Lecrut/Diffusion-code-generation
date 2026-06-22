from datetime import datetime

class DateChecker:
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def is_weekend(date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.weekday() in DateChecker.WEEKEND_DAYS

if __name__ == '__main__':
    checker = DateChecker()
    print(checker.is_weekend('2023-10-07'))
    print(checker.is_weekend('2023-10-08'))
    print(checker.is_weekend('2023-10-09'))