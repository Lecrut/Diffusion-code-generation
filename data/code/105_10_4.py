from datetime import datetime, timedelta

class DateUtils:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def next_calendar_day(date_str):
        date_obj = datetime.strptime(date_str, DateUtils.DATE_FORMAT)
        return date_obj + timedelta(days=1)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(DateUtils.next_calendar_day(sample_date))