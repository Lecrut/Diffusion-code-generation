from datetime import datetime

class DateFormatter:
    def __init__(self, date_obj):
        self.date_obj = date_obj

    def format_to_iso(self):
        return self.date_obj.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 0)
    formatter = DateFormatter(sample_dt)
    formatted_date = formatter.format_to_iso()
    print(formatted_date)