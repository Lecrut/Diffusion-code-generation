from datetime import datetime

class DateFormatter:
    LOCAL_FORMAT = '%d/%m/%Y %I:%M %p'

    @staticmethod
    def format_datetime(dt):
        return dt.strftime(DateFormatter.LOCAL_FORMAT)
if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 26, 15, 45)
    formatted_date = DateFormatter.format_datetime(sample_dt)
    print(formatted_date)