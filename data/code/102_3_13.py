import datetime

class DateChecker:
    WEEKDAY_LIMIT = 5
    
    @staticmethod
    def is_weekday(date):
        return date.weekday() < DateChecker.WEEKDAY_LIMIT

if __name__ == '__main__':
    current_date = datetime.date.today()
    print(DateChecker.is_weekday(current_date))