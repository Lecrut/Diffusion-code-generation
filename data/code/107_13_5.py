from datetime import datetime

class DateFormatter:
    def __init__(self, date_str):
        self.date_obj = datetime.strptime(date_str, '%Y/%m/%d')

    def format_date(self):
        return self.date_obj.strftime('%B %d, %Y')

if __name__ == '__main__':
    formatter = DateFormatter('2023/10/05')
    print(formatter.format_date())