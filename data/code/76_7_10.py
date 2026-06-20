from datetime import timedelta

class DateUtils:
    @staticmethod
    def add_days(date, days):
        return date + timedelta(days=days)

if __name__ == '__main__':
    from datetime import datetime
    sample_date = datetime(2023, 10, 1)
    days_to_add = 5
    result = DateUtils.add_days(sample_date, days_to_add)
    print(result)