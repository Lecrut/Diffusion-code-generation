import datetime

class DateChecker:
    WEEKDAY_LIMIT = 5
    
    @staticmethod
    def is_weekday(date_obj):
        return date_obj.weekday() < DateChecker.WEEKDAY_LIMIT

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 25)
    print(DateChecker.is_weekday(sample_date))