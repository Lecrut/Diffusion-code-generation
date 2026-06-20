from datetime import datetime

class DateDifference:
    DAYS_PER_WEEK = 7

    @staticmethod
    def calculate_weeks_difference(date1: datetime, date2: datetime) -> int:
        delta = abs((date2 - date1).days)
        return delta // DateDifference.DAYS_PER_WEEK

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 1, 15)
    print(DateDifference.calculate_weeks_difference(sample_date1, sample_date2))