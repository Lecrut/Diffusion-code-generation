from datetime import date, timedelta

class DateUtils:
    @staticmethod
    def days_between(start_date: date, end_date: date) -> int:
        return (end_date - start_date).days

if __name__ == '__main__':
    start = date(2023, 1, 1)
    end = date(2023, 12, 31)
    print(DateUtils.days_between(start, end))