from datetime import datetime

class DateTimeFormatter:
    @staticmethod
    def format_to_iso(date_obj):
        return date_obj.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    formatter = DateTimeFormatter()
    formatted_date = formatter.format_to_iso(sample_dt)
    print(formatted_date)