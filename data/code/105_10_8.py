from datetime import datetime, timedelta

class DateHandler:
    DATE_FORMAT = '%Y-%m-%d'
    
    @staticmethod
    def get_next_calendar_day(date_str):
        date_obj = datetime.strptime(date_str, DateHandler.DATE_FORMAT)
        return date_obj + timedelta(days=1)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(DateHandler.get_next_calendar_day(sample_date))