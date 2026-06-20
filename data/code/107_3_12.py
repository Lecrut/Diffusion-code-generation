from datetime import datetime

class DateFormatter:
    def format_date(self, date_obj):
        return date_obj.strftime('%a, %d %b %Y %H:%M:%S %z')

if __name__ == '__main__':
    formatter = DateFormatter()
    sample_dates = [
        datetime(2023, 10, 5),
        datetime(2024, 1, 1),
        datetime(1999, 12, 31)
    ]
    for date in sample_dates:
        print(formatter.format_date(date))