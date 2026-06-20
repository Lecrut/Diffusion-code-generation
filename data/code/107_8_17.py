from datetime import datetime

class DateFormatter:

    def format_datetime(self, dt):
        return dt.strftime('%d/%m/%Y %I:%M %p')
if __name__ == '__main__':
    formatter = DateFormatter()
    sample_date = datetime(2023, 10, 26, 15, 45)
    formatted_date = formatter.format_datetime(sample_date)
    print(formatted_date)