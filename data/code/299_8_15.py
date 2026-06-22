from datetime import date

class DateChecker:
    HOLIDAYS = {'2023-10-13', '2023-10-14', '2023-10-15'}
    
    @staticmethod
    def is_weekend_or_holiday(date_str):
        dt = date.fromisoformat(date_str)
        return dt.weekday() >= 5 or date_str in DateChecker.HOLIDAYS

if __name__ == '__main__':
    dates_to_check = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = {date: DateChecker.is_weekend_or_holiday(date) for date in dates_to_check}
    print(results)