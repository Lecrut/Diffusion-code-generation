from datetime import datetime, timedelta

class CalendarHelper:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def next_calendar_day(date_str):
        parsed_date = datetime.strptime(date_str, CalendarHelper.DATE_FORMAT)
        return parsed_date + timedelta(days=1)

if __name__ == '__main__':
    sample_date = '2023-11-15'
    result = CalendarHelper.next_calendar_day(sample_date)
    print(result)