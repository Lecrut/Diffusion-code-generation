from datetime import datetime, timedelta

class DateUtils:
    @staticmethod
    def month_after(date):
        return date.replace(day=1) + timedelta(days=40)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    print(DateUtils.month_after(sample_date))