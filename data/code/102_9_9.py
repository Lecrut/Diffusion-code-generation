import datetime

class DateChecker:
    WEEKDAY = range(5)
    
    @staticmethod
    def is_weekday(date_obj):
        return date_obj.weekday() in DateChecker.WEEKDAY
    
if __name__ == '__main__':
    dates_to_check = [
        datetime.date(2023, 10, 27),
        datetime.date(2023, 10, 28),
        datetime.date(2023, 10, 29),
        datetime.date(2023, 10, 30)
    ]
    
    for date in dates_to_check:
        print(f"Is {date} a weekday? {DateChecker.is_weekday(date)}")