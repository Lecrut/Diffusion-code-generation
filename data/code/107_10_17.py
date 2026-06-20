from datetime import datetime

class DateFormatter:
    def __init__(self, date_str):
        self.date_obj = datetime.strptime(date_str, '%Y-%m-%d')

    def format_date(self):
        return self.date_obj.strftime('%d/%m/%Y')

if __name__ == '__main__':
    sample_date = '2023-10-05'
    formatter = DateFormatter(sample_date)
    formatted_date = formatter.format_date()
    print(formatted_date)