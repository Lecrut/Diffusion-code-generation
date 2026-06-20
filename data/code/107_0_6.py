from datetime import datetime

class DateTimeFormatter:
    def format_datetime(self, dt):
        return dt.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    formatter = DateTimeFormatter()
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    formatted_date = formatter.format_datetime(sample_dt)
    print(formatted_date)