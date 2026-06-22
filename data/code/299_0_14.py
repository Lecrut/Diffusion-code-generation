from datetime import datetime

class DateHelper:
    WEEKEND_DAYS = {5, 6}

    @staticmethod
    def is_weekend(date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.weekday() in DateHelper.WEEKEND_DAYS

if __name__ == '__main__':
    print(DateHelper.is_weekend('2023-10-07'))
    print(DateHelper.is_weekend('2023-10-08'))
    print(DateHelper.is_weekend('2023-10-09'))