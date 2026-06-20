from datetime import datetime

class DateTimeFormatter:
    def __init__(self, date_obj):
        self.date_obj = date_obj

    def format_date(self, format_str='%Y-%m-%d %H:%M:%S'):
        return self.date_obj.strftime(format_str)

if __name__ == '__main__':
    dt = datetime(2023, 9, 15, 14, 30, 0)
    formatter = DateTimeFormatter(dt)
    print(formatter.format_date())
    print(formatter.format_date('%Y-%m-%d'))