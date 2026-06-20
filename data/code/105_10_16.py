from datetime import datetime, timedelta

class DateHandler:
    DATE_FORMAT = '%Y-%m-%d'
    
    @classmethod
    def get_next_calendar_day(cls, date_str):
        parsed_date = datetime.strptime(date_str, cls.DATE_FORMAT)
        return parsed_date + timedelta(days=1)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    handler = DateHandler()
    next_day = handler.get_next_calendar_day(sample_date)
    print(next_day)