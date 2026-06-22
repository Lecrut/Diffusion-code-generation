from datetime import date

class DateChecker:
    HOLIDAYS = {'2023-10-13', '2023-10-14', '2023-10-15'}

    @staticmethod
    def is_weekend_or_holiday(date_str):
        return date.fromisoformat(date_str).weekday() >= 5 or date_str in DateChecker.HOLIDAYS

if __name__ == '__main__':
    dates = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = [DateChecker.is_weekend_or_holiday(date) for date in dates]
    print(results)