from datetime import datetime

class DateFormatter:
    DATE_FORMAT = "%A, %B %d, %Y"

    @staticmethod
    def format_datetime(date_obj):
        return date_obj.strftime(DateFormatter.DATE_FORMAT)

if __name__ == '__main__':
    formatter = DateFormatter()
    sample_date = datetime(2021, 1, 1)
    formatted_date = formatter.format_datetime(sample_date)
    print(formatted_date)